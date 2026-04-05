#!/usr/bin/env bash

# ==============================================================================
# SCRIPT:        git-recover-stashes.sh
# DESCRIPCIÓN:   Busca y recupera commits de stashes perdidos (inalcanzables)
#                que Git aún no ha borrado del garbage collector.
# AUTOR:         Erlin Sangay
# FECHA:         2026-04-05
# VERSIÓN:       1.1.0
# ==============================================================================

# Configuración de colores para una mejor lectura
GREEN='\033[0;32m'
RED='\033[0;31m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # Sin color

echo -e "${CYAN}🔍 Buscando stashes perdidos en la base de datos de Git...${NC}"

# 1. Buscar hashes de commits inalcanzables que coincidan con el formato de Stash (WIP)
hashes=$(git fsck --unreachable 2>/dev/null | \
         grep commit | cut -d ' ' -f3 | \
         xargs git log --merges --no-walk --grep="WIP on" --format="%H")

if [ -z "$hashes" ]; then
    echo -e "${RED}❌ No se encontraron stashes perdidos con el formato 'WIP'.${NC}"
    exit 1
fi

# Convertir hashes en un array de forma segura
mapfile -t hash_list <<< "$hashes"

echo "--------------------------------------------------------"
echo -e "${GREEN}Se han encontrado ${#hash_list[@]} posibles stashes:${NC}"
echo "--------------------------------------------------------"

# 2. Listar información resumida de cada hash
for i in "${!hash_list[@]}"; do
    echo -e "${YELLOW}[$i] Hash: ${hash_list[$i]}${NC}"
    git log -1 --format="   📅 Fecha: %ad | 💬 %s" "${hash_list[$i]}"
    # Mostramos un resumen de archivos modificados (limitado a las primeras 5 líneas por brevedad)
    git show --stat --oneline "${hash_list[$i]}" | tail -n +2 | head -n 6
    echo "--------------------------------------------------------"
done

# 3. Inspección profunda
read -p "❓ ¿Deseas ver el contenido (diff) de alguno? (Número o 'n'): " inspect_idx

if [[ "$inspect_idx" =~ ^[0-9]+$ ]] && [ "$inspect_idx" -lt "${#hash_list[@]}" ]; then
    selected_hash=${hash_list[$inspect_idx]}
    echo -e "\n📄 Mostrando cambios en $selected_hash...\n"
    git show --first-parent "$selected_hash"
else
    echo "Siguiente paso..."
fi

# 4. Recuperación
echo -e "\n--------------------------------------------------------"
read -p "🚀 Indica el número del stash a RECUPERAR (apply) o 'q' para salir: " apply_idx

if [[ "$apply_idx" =~ ^[0-9]+$ ]] && [ "$apply_idx" -lt "${#hash_list[@]}" ]; then
    target_hash=${hash_list[$apply_idx]}
    echo -e "${GREEN}Aplicando stash $target_hash...${NC}"

    if git stash apply "$target_hash"; then
        echo -e "${GREEN}✅ Recuperado con éxito.${NC}"
    else
        echo -e "${RED}⚠️  Hubo conflictos al aplicar o el hash no es válido.${NC}"
    fi
else
    echo "Operación finalizada sin cambios."
fi
import sys
sys.path.insert(1, '..\\..\\visualization\\')

import color_gallery as cg


isaf = [cg.isaf_guinda,
        cg.isaf_dorado,
        cg.isaf_verde,
        cg.isaf_plata,
        cg.isaf_naranja,
        cg.isaf_cafe]

revista = [cg.valor_publico_vainilla,
           cg.valor_publico_amarillo,
           cg.valor_publico_cafe,
           cg.valor_publico_rojo]


print('Paletas Cargadas')
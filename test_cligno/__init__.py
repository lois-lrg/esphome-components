import esphome.codegen as cg  #importe des bibliothèques nécessaire pour compatibilité avec esphome
import esphome.config_validation as cv  #importe des bibliothèques nécessaire pour compatibilité avec esphome
from esphome.const import (
    CONF_ID,
    CONF_OUTPUT
)

#DEPENDENCIES = ['XXXX']  # si il y a une dépendance à un autre composant

light_automation_ns = cg.esphome_ns.namespace("light_automation")
Light_Automation = light_automation_ns.class_("Light_Automation", cg.PollingComponent)

CONFIG_SCHEMA = cv.Schema  # Schéma de configuration qui spécifie les paramètres nécessaires pour le composant
(
    {
        cv.GenerateID(): cv.declare_id(Light_Automation),
    }
).extend(cv.polling_component_schema("60s"))

async def to_code(config):  # convertit la configuration du composant en code C++ Esphome. Crée une nouvelle instance du composant de capteur, enregistre le composant et configure ses paramètres en fonction de la configuration fournie.
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_polling_interval(500))
    yield cg.register_component(var, config)
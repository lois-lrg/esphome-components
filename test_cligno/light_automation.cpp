#include "memory_component.h"
#include "esphome/core/log.h"
#include <Arduino.h>

#define PIN_SWITCH 32

namespace esphome {
namespace light_automation {

void Light_Automation::setup() 
{
  pinMode(PIN_SWITCH, OUTPUT); 
}
void Light_Automation::update() 
{
  digitalWrite(PIN_SWITCH, !(digitalRead(PIN_SWITCH)));   
}

float Light_Automation::get_setup_priority() const 
{
  return setup_priority::LATE;
}

}  // namespace light_automation
}  // namespace esphome
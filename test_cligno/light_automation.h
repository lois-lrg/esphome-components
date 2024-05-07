#pragma once
#include "esphome/core/component.h"

namespace esphome {
namespace light_automation {

class Light_Automation : public PollingComponent 
{
 public:
  void setup() override;
  void update() override;
  float get_setup_priority() const override;
};

}  // namespace light_automation
}  // namespace esphome
import updateTempValue from './updates/temp/updateTempValue.js';
import updateLuminosityValue from './updates/lum/updateLuminosityValue.js';
import updateWaterValue from './updates/water/updateWaterValue.js';
import updateLedValue from './updates/Led/updateLedValue.js';

eel.expose(updateTemp);
function updateTemp(TempValue){
    updateTempValue(TempValue);
}

eel.expose(updateLuminosity);
function updateLuminosity(LuminosityValue){
    updateLuminosityValue(LuminosityValue);
}


eel.expose(updateWater);
function updateWater(WaterValue){
    updateWaterValue(WaterValue);
}


eel.expose(updateLed);
function updateLed(LedValue){
    updateLedValue(LedValue);
}
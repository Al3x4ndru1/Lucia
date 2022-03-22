import updateTempValue from './updates/temp/updateTempValue.js';
import updateLuminosityValue from './updates/lum/updateLuminosityValue.js';
import updateWaterValue from './updates/water/updateWaterValue.js';
import updateLedValue from './updates/Led/updateLedValue.js';
import updateLedTurnValue from './updates/Led/updateLedValueTurn.js';

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

eel.expose(updateLedTurn);
function updateLedTurn(LedTurnValue){
    updateLedValueTurn(LedTurnValue);
}

eel.expose(charts);
function charts(chartValue){
    namescarts(chartValue);
}
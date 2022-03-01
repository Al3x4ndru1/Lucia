import updateWater from './updates/updateWater.js';
import updateLuminosity from './updates/updateLuminosity.js';
import updateTemp from './updates/temp/updateTemp.js'


eel.expose(updateTemp);
function updateTemp(TempValue){
    updateTemp(TempValue);

}

eel.expose(updateLuminosity);
function updateLuminosity(LuminosityValue){
updateLuminosity(LuminosityValue);
}

eel.expose(updateWater);
function updateWater(){

}
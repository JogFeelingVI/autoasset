/**
 * @Author: JogFeelingVI
 * @Date:   2024-03-06 15:32:30
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-03-06 15:34:26
 */
'use strict';
import * as objJs from './obj.js';
let rego_user = new objJs.swclass("yesno", "yes", "nx", true);
+ function () {
    console.log('install fixed-action-btn');
    document.addEventListener("DOMContentLoaded", (event) => {
        let acts = document.querySelectorAll('.fixed-action-btn');
        let action = M.FloatingActionButton.init(acts, '');
        /* install modal .modal */
    });
}();

// + function () {
//     let swp = new objJs.swclass("yesno", "yes", "nx", false)
//     console.log(swp)
// }();
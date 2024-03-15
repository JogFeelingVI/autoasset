/**
 * @Author: JogFeelingVI
 * @Date:   2024-03-06 15:32:30
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-03-16 00:33:22
 */
'use strict';
import * as objJs from './obj.js';
let rego_user = new objJs.swclassforjson("yesno", "yes", "nx", true);
let rego_v2 = new objJs.swclassforjson("okye", "A", "B", true);
let group_size = new objJs.radioList('GroupSizes', 'Group Size', [10, 20, 30, 50, 100, 200]);
let ranges = new objJs.meRange('ranges', 5, 1000, 5);
let groupman = new objJs.groupmanage('groupblack', 10);


+ function () {
    console.log('install fixed-action-btn');
    document.addEventListener("DOMContentLoaded", (event) => {
        let acts = document.querySelectorAll('.fixed-action-btn');
        let action = M.FloatingActionButton.init(acts, '');
        /* install modal .modal */
    });
}();

+ function () {
    group_size.setChecked = 300
    ranges.setSRV('range_value')
    ranges.setValue(35)
    groupman.datasilce()
}();
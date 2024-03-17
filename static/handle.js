/**
 * @Author: JogFeelingVI
 * @Date:   2024-01-25 20:54:21
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-03-18 00:07:15
 */
'use strict';
import * as objJs from './obj.js';
let regov2 = new objJs.swclassforjson('rego_v2', 'off', 'on', false);
let group_size = new objJs.radioList('GroupSize', 'Group Size', [5, 10, 20, 30, 50, 100, 200]);
let range_s = new objJs.meRange('rangeslider', 5, 1000, 5);
let groupman = new objJs.groupmanage('navigation', 10);
let filter_group = new objJs.filterList('filterv3');

const formatNumber = (n, x) => {
    return n.toString().padStart(Number(x), '0');
};

+ function () {
    console.log('install open edit modal');
    document.addEventListener("DOMContentLoaded", (event) => {
        let elems = document.querySelectorAll('.modal');
        let modal = M.Modal.init(elems, '');
        /* install modal .modal */
    });
}();

+ function () {
    console.log('install fixed-action-btn');
    document.addEventListener("DOMContentLoaded", (event) => {
        let acts = document.querySelectorAll('.fixed-action-btn');
        let action = M.FloatingActionButton.init(acts, '');
        /* install modal .modal */
    });
}();

+ function () {
    range_s.setSRV('slider-range-value')
    range_s.setValue(25)
}();


+ function () {
    let jsdata = JSON.parse(sessionStorage.getItem("jsdata"));
    let gs = group_size.values[0];
    if (sessionStorage.getItem('groupsize')) {
        gs = Number(sessionStorage.getItem('groupsize'))
    }
    else{
        sessionStorage.setItem('groupsize', gs)
        console.log(`groupsize is not, gs ${gs}`)
    }
    group_size.setChecked = gs
    if (!Object.is(jsdata, null)) {
        //const navigation = document.getElementById('navigation')
        groupman.datasilce(jsdata, gs)
        //installGroup(navigation, gs, jsdata)
    }
}();

+ function () {
    const gsinput = group_size.radioListEL;
    gsinput.addEventListener('change', function (e) {
        let jsdata = JSON.parse(sessionStorage.getItem('jsdata'));
        sessionStorage.setItem("groupsize", e.target.value);
        if (!Object.is(jsdata, null)) {
            //const navigation = document.getElementById('navigation')
            //installGroup(navigation, Number(e.target.value), jsdata);
            groupman.datasilce(jsdata, Number(e.target.value))
        }
    })
}();

+ function () {
    const filterv3 = document.getElementById('filterv3');
    fetch('/filter_all_name')
        .then(res => res.json())
        .then(data => {
            // console.log(data)
            // let html = ''
            // for (let i = 0; i < data.list.length; i++) {
            //     if (data.checked.indexOf(data.list[i]) != -1) {
            //         html += `<label class="offon"><input type="checkbox" checked="checked"/><span>${data.list[i]}</span></label>`
            //     } else {
            //         html += `<label class="offon"><input type="checkbox"/><span>${data.list[i]}</span></label>`
            //     }
            // }
            // filterv3.innerHTML = html
            filter_group.initForData(data)
        });
}();

function bglinear(p) {
    return `linear-gradient(to right, #d90429ff ${p}%, #8d99aeff ${p}%)`;
};

function loadInsxRego() {
    const insxrego = document.getElementById('insxrego');
    const insxsess = sessionStorage.getItem('insxrego');
    if (Object.is(insxsess, null)) {
        fetch('/load_insx_rego')
            .then(res => res.json())
            .then(data => {
                insxrego.value = data.insxd
                M.textareaAutoResize(insxrego);
                insxrego.addEventListener('input', () => {
                    sessionStorage.setItem('insxrego', insxrego.value);
                });
            });
    } else {
        insxrego.value = insxsess
    }
};

function saveInsxRego() {
    const insxsess = sessionStorage.getItem('insxrego');
    if (!Object.is(insxsess, null)) {
        let save_json = { "insxd": insxsess }
        fetch('/save_insx_rego', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(save_json)
        })
            .then(res => res.json())
            .then(data => {
                console.log(`Save to insx.rego from ${data}`);
                sessionStorage.removeItem('insxrego');
            });
    }
};

function upgradeClicked() {
    fetch('/handle')
        .then(res => res.json())
        .then(data => {
            const formattedData = `${data.message}, <span>${data.Last}</span>, <lable>${data.time}</lable>.`;
            document.getElementById('upgrade_data').innerHTML = formattedData;
        });
};

function doneClicked() {
    // const filterv3 = document.getElementById('filterv3');
    // const labels = filterv3.getElementsByTagName('label');
    const checkboxStates = { 'rego': regov2.checked, 'range': range_s.value}
    const filterCheck = filter_group.getCheckedAll()
    Object.entries(filterCheck).forEach(([name, check])=>{
        checkboxStates[name] = check
    })
    const json = JSON.stringify(checkboxStates);
    console.log(`json -> ${json}`)
    PostJson(json);
};

function runing() {
    let rings = document.getElementById("runing");
    let value = parseFloat(rings.innerHTML) + 0.1;
    rings.innerHTML = value.toFixed(1);
};

function PostJson(JSONA) {
    const navigation = document.getElementById('navigation')
    let times = setInterval("runing()", 100);
    navigation.innerHTML = `<div id="runing">0.0</div>`;
    fetch('/handle_post', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(JSONA)
    })
        .then(res => res.json())
        .then(data => {
            const jsdata = JSON.parse(data)
            
            sessionStorage.setItem('jsdata', data);
            let item = ''
            navigation.innerHTML = item
            let GroupS = sessionStorage.getItem("groupsize");
            clearInterval(times);
            //installGroup(navigation, Number(GroupS), jsdata)
            groupman.datasilce(jsdata, Number(GroupS))
        });
};


function donwLoadGroup() {
    /* div.listmgs:nth-child(1) */
    console.log(`donwload click`);
    const groups = document.querySelectorAll("div.group");
    groups.forEach((item, index, array) => {
        item.classList.remove("anmin");
        html2canvas(item, {
            "backgroundColor": "#2b2d42ff",
            "allowTaint": false,
            "scale": 4,
        }).then(canvas => {
            /*
            document.body.appendChild(canvas);
            */
            const b64image = canvas.toDataURL("image/png");
            let donwlink = document.createElement("a");
            donwlink.setAttribute("href", b64image);
            donwlink.setAttribute("download", `Group_${formatNumber(index + 1, 3)}_${objJs.pickRandomChars(5)}.png`);
            donwlink.click();
            donwlink.remove();
        });
    });
};

window.doneClicked = doneClicked
window.donwLoadGroup = donwLoadGroup
window.upgradeClicked = upgradeClicked
window.runing = runing
window.saveInsxRego = saveInsxRego
window.bglinear = bglinear
window.loadInsxRego = loadInsxRego


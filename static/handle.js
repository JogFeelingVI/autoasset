/**
 * @Author: JogFeelingVI
 * @Date:   2024-01-25 20:54:21
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-02-12 23:47:28
 */
'use strict';
document.addEventListener("DOMContentLoaded", (event) => {
    console.log("DOM fully loaded and parsed");
    let elems = document.querySelectorAll('.modal');
    let modal = M.Modal.init(elems, '');

    let acts = document.querySelectorAll('.fixed-action-btn');
    let action = M.FloatingActionButton.init(acts, '');

    const sliderEl = document.querySelector("#slider");
    const sliderValue = document.querySelector("#slider-range-value");
    sliderValue.innerHTML = sliderEl.value
    let progress = (sliderEl.value / sliderEl.max) * 100;
    sliderEl.style.background = bglinear(progress);

    sliderEl.addEventListener("input", (event) => {
        const tempSliderValue = event.target.value;
        sliderValue.textContent = tempSliderValue;

        progress = (tempSliderValue / sliderEl.max) * 100;
        sliderEl.style.background = bglinear(progress);
    });

    let jsdata = JSON.parse(sessionStorage.getItem("jsdata"));
    let gs = sessionStorage.getItem("groupsize");
    if (!Object.is(gs, null)) {
        gs = Number(gs)
    }
    else {
        gs = 5
    }
    /* 
    document.querySelector("#GroupSize > label:nth-child(4) > input[type=radio]")
    #GroupSize > label:nth-child(4) > input[type=radio]
    #GroupSize > label:nth-child(6) > input[type=radio]
     */
    let cked = document.querySelector(`#GroupSize > label:nth-child(${gs/5+1}) > input[type=radio]`);
    cked.checked = true;
    console.log(cked);   
    if (!Object.is(jsdata, null)) {
        const navigation = document.getElementById('navigation')
        installGroup(navigation, gs, jsdata)
    }

});

const gsinput = document.querySelector('#GroupSize');
gsinput.addEventListener('change', function (e) {
    let jsdata = JSON.parse(sessionStorage.getItem('jsdata'));
    sessionStorage.setItem("groupsize", e.target.value)
    if (!Object.is(jsdata, null)) {
        const navigation = document.getElementById('navigation')
        installGroup(navigation, Number(e.target.value), jsdata)
    }
});

window.onload = function () {
    const filterv3 = document.getElementById('filterv3');
    fetch('/filter_all_name')
        .then(res => res.json())
        .then(data => {
            let html = ''
            for (let i = 0; i < data.list.length; i++) {
                if (data.checked.indexOf(data.list[i]) != -1) {
                    html += `<label class="offon"><input type="checkbox" checked="checked"/><span>${data.list[i]}</span></label>`
                } else {
                    html += `<label class="offon"><input type="checkbox"/><span>${data.list[i]}</span></label>`
                }
            }
            filterv3.innerHTML = html
        });
};

function bglinear(p) {
    return `linear-gradient(to right, #d90429ff ${p}%, #8d99aeff ${p}%)`;
}

function loadInsxRego() {
    fetch('/load_insx_rego')
        .then(res => res.json())
        .then(data => {
            const save = document.getElementById('insxrego')
            save.value = data.insxd
            M.textareaAutoResize(save);
        });
};

function saveInsxRego() {
    const save = document.getElementById('insxrego').value
    let save_json = { "insxd": save }
    fetch('/save_insx_rego', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(save_json)
    })
        .then(res => res.json())
        .then(data => {
            console.log(data)
        });
};

function upgradeClicked() {
    fetch('/handle')
        .then(res => res.json())
        .then(data => {
            const formattedData = `${data.message}, ${data.time}.`;
            document.getElementById('upgrade_data').innerHTML = formattedData;
        });
};

function doneClicked() {
    const rangeValue = document.getElementById('slider-range-value')
    const rego = document.getElementById('rego')
    const filterv3 = document.getElementById('filterv3');
    const labels = filterv3.getElementsByTagName('label');
    const onoff = rego.getElementsByTagName('input')[0]
    const checkboxStates = { 'rego': onoff.checked, 'range': Number(rangeValue.innerText) }
    for (let i = 0; i < labels.length; i++) {
        let ckb = labels[i].getElementsByTagName('input')[0];
        let span = labels[i].getElementsByTagName('span')[0];
        if (ckb.checked) {
            checkboxStates[span.innerHTML] = ckb.checked
        }
    }
    const json = JSON.stringify(checkboxStates);
    PostJson(json);
};

function PostJson(JSONA) {
    const navigation = document.getElementById('navigation')
    /* navigation.innerHTML = `<p>json data has been sent waiting for server response.</p>` */
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
            /*
            for (let it in jsdata) {
                let ix = jsdata[it]
                item = `<div class="message anmin"><span class="r-text">${ix[0]}</span><span class="b-text">${ix[1]}</span></div>`
                navigation.innerHTML += item;
            }*/

            const labels = document.querySelectorAll('#GroupSize label');
            let GroupS = 5
            labels.forEach((label) => {
                const isChecked = label.querySelector('input');
                if (isChecked.checked) {
                    GroupS = Number(isChecked.value);
                    return;
                }
            });
            installGroup(navigation, GroupS, jsdata)
        });
};

function installGroup(nav, size, data) {
    const indexData = [];
    for (let index in data) {
        indexData.push(index);
    }
    const groupedData = [];
    nav.innerHTML = ''
    for (let i = 0; i < indexData.length; i += size) {
        groupedData.push(indexData.slice(i, i + size));
    }
    groupedData.forEach((item, index) => {
        let htx = `<div class="listmgs anmin">
        <div class="haed"><span class="a">Group</span> <span class="r">${Number(index) + 1}</span></div>
        <div class="spa"></div>`
        item.forEach((it, inx, arr) => {
            let ix = data[it]
            htx += `<div><span class="r">${ix[0]}</span> <span class="b">${ix[1]}</span></div>`
            if ((inx + 1) % 5 === 0 && inx !== arr.length - 1) {
                htx += `<div class="spb"></div>`
            }
        });
        htx += `</div><!--end message -->`
        nav.innerHTML += htx
    });
};

function donwLoadGroup() {
    /* div.listmgs:nth-child(1) */
    console.log(`donwload click`);
    const groups = document.querySelectorAll("div.listmgs");
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
            Canvas2Image.saveAsPNG(canvas);
        });
    });
};


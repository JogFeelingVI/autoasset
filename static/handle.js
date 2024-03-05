/**
 * @Author: JogFeelingVI
 * @Date:   2024-01-25 20:54:21
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-03-05 09:06:30
 */
'use strict';

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

// + function () {
//     const sliderEl = document.querySelector("#slider");
//     const sliderValue = document.querySelector("#slider-range-value");
//     sliderValue.innerHTML = sliderEl.value
//     let progress = (sliderEl.value / sliderEl.max) * 100;
//     sliderEl.style.background = bglinear(progress);

//     sliderEl.addEventListener("input", (event) => {
//         const tempSliderValue = event.target.value;
//         sliderValue.textContent = tempSliderValue;

//         progress = (tempSliderValue / sliderEl.max) * 100;
//         sliderEl.style.background = bglinear(progress);
//     });
// }();

+ function () {
    let sliderValue = document.querySelector("#slider-range-value");
    let slider = document.getElementById('rangeslider');
    let slider_width = slider.getBoundingClientRect().width;
    let shoubing = slider.getElementsByClassName("shoubing")[0]
    let showbing_width = shoubing.getBoundingClientRect().width
    // .meRange .huagui .shoubing:before
    let Attributes = slider.getElementsByTagName("Attributes")[0]
    let max = Number(Attributes.getAttribute("max"))
    let min = Number(Attributes.getAttribute("min"))
    let step = Number(Attributes.getAttribute("step"))
    let value = Number(Attributes.getAttribute("value"))
    // 需要用到的变量
    
    function setValue(number){
        // dangqian /(max-min)*slider_wider
        let left = number / (max-min) * slider_width
        shoubing.style.left = left + 'px';
        shoubing.style.setProperty('--oks', left + 'px')
        shoubing.style.setProperty('--okb', -left + 'px')
        sliderValue.innerHTML = number
    }


    shoubing.addEventListener("mousedown", function (event) {
        let initialX = event.clientX;
        function moveElement(event) {
            let currentX = event.clientX;
            let deltaX = currentX - initialX;
            let dangqian = shoubing.offsetLeft + deltaX
            let max_left = slider_width - showbing_width
            if (dangqian >= 0 && dangqian <= max_left) {
                shoubing.style.left = dangqian + 'px';
                // 设置进度条背景
                shoubing.style.setProperty('--oks', dangqian + 'px')
                shoubing.style.setProperty('--okb', -dangqian + 'px')
                let bili = dangqian / max_left * (max - min) + min
                bili = roundToStep(bili, step)
                initialX = currentX;
                Attributes.setAttribute("value", bili);
                sliderValue.innerHTML = bili
            };
        };

        function roundToStep(number, step) {
            // 将数字格式化成 step的倍数
            if (number % step === 0) {
                return number;
            } else {
                return Math.ceil(number / step) * step;
            }
        };

        function stopElement(event) {
            document.removeEventListener('mousemove', moveElement);
            document.removeEventListener('mouseup', stopElement);
        };

        document.addEventListener('mousemove', moveElement);
        document.addEventListener('mouseup', stopElement);
    });
    setValue(value);
}();



+ function () {
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
    let cked = document.querySelector(`#GroupSize > label:nth-child(${gs / 5 + 1}) > input[type=radio]`);
    cked.checked = true;
    if (!Object.is(jsdata, null)) {
        const navigation = document.getElementById('navigation')
        installGroup(navigation, gs, jsdata)
    }
}();

+ function () {
    const gsinput = document.querySelector('#GroupSize');
    gsinput.addEventListener('change', function (e) {
        let jsdata = JSON.parse(sessionStorage.getItem('jsdata'));
        sessionStorage.setItem("groupsize", e.target.value);
        if (!Object.is(jsdata, null)) {
            const navigation = document.getElementById('navigation')
            installGroup(navigation, Number(e.target.value), jsdata);
        }
    })
}();

+ function () {
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
}();

function bglinear(p) {
    return `linear-gradient(to right, #d90429ff ${p}%, #8d99aeff ${p}%)`;
}

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

function runing() {
    let rings = document.getElementById("runing");
    let value = parseFloat(rings.innerHTML) + 0.1;
    rings.innerHTML = value.toFixed(1);
}

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
            clearInterval(times);
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

function pickRandomChars(numChars) {
    // 将字符串转换为数组
    const arr = 'aBshiuyRfhklMezx1235670'.split('');
    // 初始化一个空数组来存储随机挑选的字符
    const pickedChars = [];

    // 随机挑选指定数量的字符
    for (let i = 0; i < numChars; i++) {
        // 生成一个随机索引
        const randomIndex = Math.floor(Math.random() * arr.length);

        // 将随机索引处的字符添加到 pickedChars 数组
        pickedChars.push(arr[randomIndex]);

        // 从 arr 数组中删除该字符，避免重复选择
        arr.splice(randomIndex, 1);
    }

    // 将 pickedChars 数组转换为字符串并返回
    return pickedChars.join('');
}

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
            const b64image = canvas.toDataURL("image/png");
            let donwlink = document.createElement("a");
            donwlink.setAttribute("href", b64image);
            donwlink.setAttribute("download", `Group_${formatNumber(index + 1, 3)}_${pickRandomChars(5)}.png`);
            donwlink.click();
            donwlink.remove();
        });
    });
};


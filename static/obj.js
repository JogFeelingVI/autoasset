'use strict';

export function pickRandomChars(numChars) {
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
};

export class swclass {
    constructor(idx, qs, hs, check) {
        this.input_id = `swclass_${pickRandomChars(5)}`
        let divid = document.getElementById(idx)
        divid.classList.add("sw")
        let label = document.createElement("label")
        label.setAttribute("for", this.input_id)

        let qian = document.createElement("div")
        qian.classList.add('qian')
        qian.append(qs)

        let see = document.createElement("div")
        see.classList.add('see')

        this.input_check = document.createElement("input")
        this.input_check.setAttribute("id", this.input_id)
        this.input_check.setAttribute("type", "checkbox")
        if (check) {
            this.input_check.setAttribute("checked", "")
        }

        let div_bg = document.createElement("div")
        div_bg.classList.add("bg")
        let div_shou = document.createElement("div")
        div_shou.classList.add("shou")
        see.append(this.input_check, div_bg, div_shou)


        let hou = document.createElement('div')
        hou.classList.add('hou')
        hou.append(hs)

        label.append(qian, see, hou)
        divid.append(label)
        console.log(`Object id ${this.input_id} Creation completed.`)
    }

    get id() {
        return this.input_id
    }

    get checked() {
        return this.input_check.checked
    }
}


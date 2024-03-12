/**
 * @Author: JogFeelingVI
 * @Date:   2024-03-10 20:50:31
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-03-12 15:15:23
 */
'use strict';

export function pickRandomChars(numChars = 5) {
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
    constructor(idx = 'id', qs = 'yes', hs = 'no', check = false) {
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

export class radioList {
    constructor(idx = 'id', Comment = 'radioList', items = [10, 20, 50, 100, 200]) {
        this.radioListEL = document.getElementById(idx)
        this.radioListEL.classList.add('radioList')
        this.values = items
        if (!Object.is(this.radioListEL, null)) {
            if (!Object.is(Comment, null)) {
                this.radioListEL.append(this.init_Comment(Comment))
                this.name = pickRandomChars(5)
                this.items_inx = 0
                items.forEach((v, i) => {
                    let EL = this.init_items(v, i)
                    this.radioListEL.append(EL)
                })
            }
        }
    }

    get checkItem() {
        let inputs = this.radioListEL.getElementsByTagName('input')
        Array.from(inputs).forEach((v, i) => {
            if (v.checked) {
                return v
            }
        })
    }

    set setChecked(value = 5) {
        if (!this.values.includes(value)){
            value = this.values[0]
        }
        let inputs = this.radioListEL.getElementsByTagName('input')
        Array.from(inputs).forEach((v, i) => {
            if (v.getAttribute('value') === `${value}`) {
                v.checked = true
                return v
            }
        })
    }

    init_Comment(c = 'info') {
        // c = Comment 注释说明
        let comEL = document.createElement('span')
        comEL.innerHTML = c
        return comEL
    }

    init_items(i = 5, index = 10) {
        // i shuzhi 5 6 8 9 10 deng
        // <label>
        //     <input name="gs" type="radio" value="15" />
        //     <span>15</span>
        // </label>
        let labelEL = document.createElement('label')
        let input = document.createElement('input')
        let span = document.createElement('span')
        input.setAttribute('name', this.name)
        input.setAttribute('type', 'radio')
        input.setAttribute('value', i)
        if (index === this.items_inx) {
            input.setAttribute('checked', '')
        }
        span.innerHTML = i
        labelEL.append(input, span)
        return labelEL
    }
}

export class meRange{
    // <div id="rangeslider" class="meRange">
    //     <div class="huagui_bg">
    //     <Attributes min="5", max="1000", value="25", step="5">
    //     </div>
    //     <div class="huagui">
    //     <div class="shoubing"></div>
    //     </div>
    // </div>
    constructor(idx='id',){
        
    }
}



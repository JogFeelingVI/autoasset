/**
 * @Author: JogFeelingVI
 * @Date:   2024-03-10 20:50:31
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-03-14 00:23:41
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

    checkItem() {
        let inputs = this.radioListEL.getElementsByTagName('input')
        Array.from(inputs).forEach((v, i) => {
            if (v.checked) {
                return Number(v.getAttribute('value'))
            }
        })
    }

    set setChecked(value = 5) {
        if (!this.values.includes(value)) {
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

export class meRange {
    // <div id="rangeslider" class="meRange">
    //     <div class="huagui_bg">
    //     <Attributes min="5", max="1000", value="25", step="5">
    //     </div>
    //     <div class="huagui">
    //          <div class="shoubing"></div>
    //     </div>
    // </div>
    constructor(idx = 'id', min = 5, max = 1000, step = 5) {
        this.sliderValue = null
        this.range = document.getElementById(idx)
        this.range.classList.add('meRange')
        this.range_width = this.range.getBoundingClientRect().width
        let cls_name = ['huagui_bg', 'huagui']
        if (!Object.is(this.range, null)) {
            cls_name.forEach((v, i, arr) => {
                let temp = this.init_div(v)
                if (v === 'huagui_bg') {
                    this.attr = this.init_Attributes(min, max, step)
                    temp.append(this.attr)
                }
                if (v === 'huagui') {
                    this.shoubing = this.init_div('shoubing')
                    temp.append(this.shoubing)
                }
                this.range.append(temp)
            })
        }
        this.range_max_width = this.range_width - this.shoubing.getBoundingClientRect().width
        this.doStart = e => { return this.startDrag(e) }
        this.doMove = e => { return this.moveDrag(e) }
        this.doEnd = e => { return this.endDrag(e) }
        this.shoubing.addEventListener('mousedown', this.doStart)
    }

    setSRV(idx = 'slider-range-value') {
        // 在web app 上显示当前数值
        let srv = document.getElementById(idx)
        if (!Object.is(srv, null)) {
            this.sliderValue = srv
        } else {
            console.log(`setting SRV done.`)
        }
    }

    echo(val = 25) {
        // 社会元素sliderValue为输出元素
        if (!Object.is(this.sliderValue, null)) {
            this.sliderValue.innerText = val
        }
    }

    setValue(val = 25) {
        // 启动的时候使用
        this.attr.setAttribute('value', val)
        let left = val / (this.max - this.min) * this.range_max_width
        this.shoubing.style.left = `${left}px`;
        this.shoubing.style.setProperty('--oks', `${left}px`)
        this.shoubing.style.setProperty('--okb', `-${left}px`)
        this.echo(val)
        return val
    }


    get min() {
        return Number(this.attr.getAttribute('min'))
    }

    get max() {
        return Number(this.attr.getAttribute('max'))
    }

    get value() {
        return Number(this.attr.getAttribute('value'))
    }

    get step() {
        return Number(this.attr.getAttribute('step'))
    }


    shoubing_left(left = 65) {
        this.shoubing.style.left = `${left}px`;
        this.shoubing.style.setProperty('--oks', `${left}px`)
        this.shoubing.style.setProperty('--okb', `-${left}px`)
        let bili = left / this.range_max_width * (this.max - this.min) + this.min
        bili = this.roundToStep(bili, this.step)
        this.attr.setAttribute('value', bili)
        this.echo(bili)
    }

    roundToStep(number = 5, step = 5) {
        // 将数字格式化成 step的倍数
        if (number % step === 0) {
            return number;
        } else {
            return Math.ceil(number / step) * step;
        }
    }

    init_Attributes(min = 5, max = 1000, step = 5) {
        let attr = document.createElement('attributes')
        attr.setAttribute('min', min)
        attr.setAttribute('max', max)
        attr.setAttribute('value', min)
        attr.setAttribute('step', step)
        return attr
    }

    init_div(cls = 'huagui_bg') {
        let div = document.createElement('div')
        div.classList.add(cls)
        return div
    }

    startDrag(event) {
        this.startX = event.clientX
        // console.log(`startDrag ${event.clientX}`)
        document.addEventListener('mousemove', this.doMove);
        document.addEventListener('mouseup', this.doEnd);
    }

    moveDrag(event) {
        // let getStyle = window.getComputedStyle(this.shoubing);
        // let leftVal = parseInt(getStyle.left) + (event.clientX - this.startX);
        let leftVal = this.shoubing.offsetLeft + (event.clientX - this.startX);
        // console.log(`moveDrag ${leftVal}`)
        if (leftVal >= 0 && leftVal <= this.range_max_width) {
            this.shoubing_left(leftVal)
        };
        this.startX = event.clientX
    }

    endDrag(event) {
        // console.log(`endDrag ${event}`)
        document.removeEventListener('mousemove', this.doMove);
        document.removeEventListener('mouseup', this.doEnd);
    }
}



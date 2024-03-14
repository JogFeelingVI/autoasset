/**
 * @Author: JogFeelingVI
 * @Date:   2024-03-10 20:50:31
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-03-14 22:37:09
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

export class swclassforjson {
    // 根据map信息生产新的元素结构体
    constructor(idx = 'idx', before = '', after = '', check = false) {
        this.inputidx = `swclass_${pickRandomChars(5)}`
        this.main = document.getElementById(idx)
        this.before = before
        this.after = after
        this.check = check
        this.makeupEL()
    }

    makeupEL() {
        // 按照图纸制造结构体
        //document.createElement
        let Jsmap = this.makeup_Obj()
        Jsmap.forEach((items) => {
            let reitem = this.makeuped(items)
            if (!Object.is(reitem, null)) {
                this.main.append(reitem)
            }
        })
        console.log(`swclass obg makeup done ${this.inputidx}`)
    }

    get checked() {
        let check = document.getElementById(this.inputidx).checked
        return check
    }

    

    makeup_Obj() {
        let objmap = [
            {
                'tag': 'main', 'class': 'sw', 'child': [
                    {
                        'tag': 'label', 'for': 'id', 'child': [
                            { 'tag': 'div', 'class': 'qian', 'append': 'before' },
                            {
                                'tag': 'div', 'class': 'see', 'child': [
                                    { 'tag': 'input', 'type': 'checkbox', 'id': 'id', 'checked': false },
                                    { 'tag': 'div', 'class': 'bg' },
                                    { 'tag': 'div', 'class': 'shou' }
                                ]
                            },
                            { 'tag': 'div', 'class': 'hou', 'append': 'after' },
                        ]
                    },
                ]
            }
        ]
        return objmap
    }

    makeuped(item = { 'tag': 'div', 'class': 'sw' }) {
        let keys = Object.keys(item)
        if (keys.includes('tag')) {

            if (item['tag'] === 'main') {
                this.main.classList.add('sw')
                let itemm = item['child']
                itemm.forEach((item) => {
                    this.main.append(this.makeuped(item))
                })
                return null
            }

            let el = document.createElement(item['tag'])

            if (keys.includes('class')) {
                el.classList.add(item['class'])
            }
            if (keys.includes('for')) {
                el.setAttribute('for', this.inputidx)
            }
            if (keys.includes('id')) {
                el.setAttribute('id', this.inputidx)
            }
            if (keys.includes('append')) {
                let flg = item['append']
                if (flg === 'before') {
                    el.innerHTML = this.before
                }
                if (flg === 'after') {
                    el.innerHTML = this.after
                }
            }
            if (keys.includes('type')) {
                el.setAttribute('type', item['type'])
            }
            if (keys.includes('checked')) {
                if (this.check === true) {
                    el.setAttribute('checked', '')
                }
            }
            if (keys.includes('child')) {
                let child = item['child']
                child.forEach((item_child) => {
                    el.append(this.makeuped(item_child))
                })
            }
            return el
        }
        return null
    }
    // 生成机构体需要的图纸 json
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


export class groupmanage {
    // <div class="listmgs anmin">
    //     <div class="haed"><span class="a">Group</span> <span class="r">7</span></div>
    //     <div class="spa"></div>
    //     <div><span class="r">07 12 14 19 23 32</span> <span class="b">14</span></div>
    //     <div><span class="r">07 14 16 19 22 32</span> <span class="b">16</span></div>
    //     <div><span class="r">05 14 17 19 22 28</span> <span class="b">14</span></div>
    //     <div><span class="r">07 10 12 13 23 29</span> <span class="b">12</span></div>
    //     <div><span class="r">07 11 14 19 24 28</span> <span class="b">14</span></div>
    //     <div class="spb"></div>
    //     <div><span class="r">05 10 12 19 21 28</span> <span class="b">14</span></div>
    //     <div><span class="r">05 13 16 19 24 32</span> <span class="b">16</span></div>
    // </div>
}

export class gitem {
    // <div><span class="r">07 14 16 19 22 32</span> <span class="b">16</span></div>
}


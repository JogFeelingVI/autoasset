## autoasseting
> 根据设置自动化的产生号码,这些核心包含REGO,FILTER,POSTCALL等模块化核心。
> `poetry run python ./app.py`

### setings
```python
    js = '{"rego":true,"acvalue":true,"dx16":true,"mod2":true,"mod3":true,"mod4":true,"mod5":true,"mod6":true,"mod7":true,"sixlan":true,"zhihe":true,"lianhao":true}'
    p = `postcall`
    p.initPostCall()
    p.instal_json(js=js)
    p.setting_length(500)
    p.tasks_futures()
    # p.tasks_Queue() 
    for k, v in p.todict().items():
        n, t = v
        print(f'[{k:>3}] {n} + {t}')
```

* rego insx.rego 在网页上可以直接编辑。
* filter 设置了好几种常见的过滤器,通过filterN_v3.json来设置，但是可以通过网页来关闭启用。


```json
{
    "name": "dzx",
    "Optional": [0,1,2,3,4,5,6],
    "recommend": [0,1,2,3,4],
    "checked": false,
    "Description": "d is 23-33, z is 12-22,x is 1-11."
}
```
#### json info
* `name` 过滤器名称
* `Optional` 可以使用的选项
* `checked` False ot True
* `Description` info....
* `__commant__` commant...

#### Custom range input
```html
<div class="example">
    <div id="rangeslider" class="noUi-target noUi-ltr noUi-horizontal noUi-txt-dir-ltr">
        <div class="noUi-base">
            <div class="noUi-connects"></div>
            <div class="noUi-origin" style="transform: translate(-80.9868%, 0px); z-index: 4;">
                <div class="noUi-handle noUi-handle-lower" data-handle="0" tabindex="0" role="slider" aria-orientation="horizontal" aria-valuemin="5.0" aria-valuemax="1000.0" aria-valuenow="194.2" aria-valuetext="194.18">
                    <div class="noUi-touch-area"></div>
                </div>
            </div>
        </div>
    </div>
</div>
```
#### Style CSS
* `transform` 
  > transform: translate(0%, 0px); z-index: 4;
```css
/* html root color*/
input[type="range"] {
    /* removing default appearance */
    -webkit-appearance: none;
    appearance: none;
    /* creating a custom design */
    width: 100%;
    cursor: pointer;
    outline: none;
    border: none;
    height: 1px;
    background-color: var(--cool-gray);
}

input[type="range"]::-webkit-slider-runnable-track {
    width: 100%;
    height: 3px;
    cursor: pointer;
    background: transparent;
}

input[type="range"]::-moz-range-track {
    width: 100%;
    height: 3px;
    cursor: pointer;
    background: transparent;
}

/* Thumb: webkit */
input[type="range"]::-webkit-slider-thumb {
    /* removing default appearance */
    -webkit-appearance: none;
    appearance: none;
    /* creating a custom design */
    height: 15px;
    width: 15px;
    background-color: var(--red-pantone);
    border-radius: 50%;
    border: none;
    /* box-shadow: -407px 0 0 400px #f50; emove this line */
    transition: .2s ease-in-out;
}

/* Thumb: Firefox */
input[type="range"]::-moz-range-thumb {
    height: 15px;
    width: 15px;
    background-color: var(--red-pantone);
    border-radius: 50%;
    border: none;
    /* box-shadow: -407px 0 0 400px #f50; emove this line */
    transition: .2s ease-in-out;
}
```
##### Use custom range
![运行时效果图](248ob-nplil.gif "Use custom range")
###### html
```html
 <div class="example">
    <div id="rangeslider" class="meRange">
        <div class="huagui_bg">
        <Attributes min="5", max="1000", value="25", step="5">
        </div>
        <div class="huagui">
        <div class="shoubing"></div>
        </div>

    </div>
</div>
```
###### CSS
```css

.meRange {
    display: inline-block;
    box-sizing: content-box;
    width: 100%;
    background: transparent;
    transform: rotate(0);
    user-select: none;
}

.meRange .huagui_bg {
    position: absolute;
    width: 100%;
    height: 1px;
    top: 50%;
    -webkit-transform: translate(0, 50%);
    transform: translate(0, -50%);
    background: var(--cool-gray);
}

.meRange .huagui_bg>* {
    /* min max setp hide */
    display: none
}

.meRange .huagui {
    width: 100%;
}

.meRange .huagui .shoubing {
    display: block;
    position: relative;
    height: 16px;
    width: 16px;
    border-radius: 50%;
    -webkit-transform: translate(0px, 0);
    transform: translate(0px, 0);
    background-color: var(--fire-engine-red);
}

.meRange .huagui .shoubing:before {
    content: "";
    position: absolute;
    top: 50%;
    -webkit-transform: translate(0, 50%);
    transform: translate(0, -50%);
    width: var(--oks, 0);
    left: var(--okb, 0);
    /* -left = width = shoubing.width */
    height: 3px;
    background-color: aqua;
}
```
###### javascript
```javascript
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
```

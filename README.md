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
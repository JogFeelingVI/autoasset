<!---->
{% for item in navigation|batch(5) %}
<div class="itemx">
    <span class="Tiny material-icons blue-text lighten-4">
    list
    </span>
    {% for column in item %}
    <div class="message">
        <span class="grey-text darken-3">{{ column.number|join(" ") }}</span>
        <span class="blue-text darken-4">{{ column.tiebie|join(" ") }}</span>
    </div>
    {% endfor %}
    
</div>
{% endfor %}
<!---->

{% for item in navigation %}
    <div class="message">
        <span class="red-text darken-3">{{ item.number|join(" ") }}</span>
        <span class="blue-text darken-4">{{ item.tiebie|join(" ") }}</span>
    </div>
{% endfor %}


<label class="container">Keep me up to date on news and offers
    <input type="checkbox" id="checkbox">
    <span class="checkmark"></span>
</label>

curl -L {url} -o ./config.json

https://sing-box-subscribe-sable-psi.vercel.app/config/url=https://42.194.232.60:10387/iplist/kHZenqIKxqRgKgdU?clash=2&new=1&file=https://gist.githubusercontent.com/yangchuansheng/5182974442015feeeeb058de543a00fd/raw/45b11ff08188af021da98e7174923d719dc42dd9/gistfile1.txt
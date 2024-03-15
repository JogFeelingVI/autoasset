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

function invertHslColor(hslColor) {
  // 將 HSL 顏色轉換為 RGB 顏色
  const rgb = hslToRgb(hslColor);

  // 對於每個 RGB 通道，計算其反轉值
  const invertedRgb = {
    r: 255 - rgb.r,
    g: 255 - rgb.g,
    b: 255 - rgb.b,
  };

  // 將反轉的 RGB 值轉換回 HSL 顏色
  return rgbToHsl(invertedRgb);
}

// HSL 轉換為 RGB 的函數
function hslToRgb(hsl) {
  const [h, s, l] = hsl;

  const c = (1 - Math.abs(2 * l - 1)) * s;
  const x = c * (1 - Math.abs((h / 60) % 2 - 1));
  const m = l - c / 2;

  let r, g, b;
  if (h >= 0 && h < 60) {
    r = c;
    g = x;
    b = 0;
  } else if (h >= 60 && h < 120) {
    r = x;
    g = c;
    b = 0;
  } else if (h >= 120 && h < 180) {
    r = 0;
    g = c;
    b = x;
  } else if (h >= 180 && h < 240) {
    r = 0;
    g = x;
    b = c;
  } else if (h >= 240 && h < 300) {
    r = x;
    g = 0;
    b = c;
  } else if (h >= 300 && h < 360) {
    r = c;
    g = 0;
    b = x;
  }

  r = Math.round((r + m) * 255);
  g = Math.round((g + m) * 255);
  b = Math.round((b + m) * 255);

  return { r, g, b };
}

// RGB 轉換為 HSL 的函數
function rgbToHsl(

curl -L {url} -o ./config.json

https://sing-box-subscribe-sable-psi.vercel.app/config/url=https://42.194.232.60:10387/iplist/kHZenqIKxqRgKgdU?clash=2&new=1&file=https://gist.githubusercontent.com/yangchuansheng/5182974442015feeeeb058de543a00fd/raw/45b11ff08188af021da98e7174923d719dc42dd9/gistfile1.txt
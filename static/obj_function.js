/**
 * @Author: JogFeelingVI
 * @Date:   2024-03-15 13:47:58
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-03-15 15:43:38
 */

function autopicker() {
    let hsl_a = generateHslColor_67()
    let hsl_c = buserHslColor(hsl_a)
    return [hslToStr(hsl_a), hslToStr(hsl_c)]
}

function generateHslColor() {
    const h = Math.floor(Math.random() * 360);
    const s = Math.floor(Math.random() * 100);
    const l = Math.floor(Math.random() * 100);
    return [h, s, l];
}

function generateHslColor_67() {
    const h = Math.floor(Math.random() * 360);
    const s = 67;
    const l = 85;
    return [h, s, l];
}

function hslToStr(hsl) {
    const [h, s, l] = hsl
    return `hsl(${h}, ${s}%, ${l}%)`
}

function buserHslColor(hslColor = [233, 30, 30]) {
    let [h,s,l] = hslColor
    s= 100-s
    return [h,s,l]
}

function invertHslColor(hslColor = [233, 0.3, 0.3]) {
    // 將 HSL 顏色轉換為 RGB 顏色
    const rgb = hslToRgb(hslColor);

    // 對於每個 RGB 通道，計算其反轉值
    const invertedRgb = [
        255 - Number(rgb[0]),
        255 - Number(rgb[1]),
        255 - Number(rgb[2]),
    ]
    //console.log(`fanse ${rgb} = ${invertedRgb}`)
    // 將反轉的 RGB 值轉換回 HSL 顏色
    return rgbToHsl(invertedRgb);
}

// HSL 轉換為 RGB 的函數
function hslToRgb(hsl) {
    let [h, s, l] = hsl;

    s = s / 100;
    l = l / 100;
    const k = n => (n + h / 30) % 12;
    const a = s * Math.min(l, 1 - l);
    const f = n =>
        l - a * Math.max(-1, Math.min(k(n) - 3, Math.min(9 - k(n), 1)));
    return [parseInt(255 * f(0)), parseInt(255 * f(8)), parseInt(255 * f(4))];
}

// RGB 轉換為 HSL 的函數
function rgbToHsl(rgb = [255, 255, 255]) {
    let [r, g, b] = rgb;

    r /= 255;
    g /= 255;
    b /= 255;
    let l = Math.max(r, g, b);
    let s = l - Math.min(r, g, b);
    let h = s
        ? l === r
            ? (g - b) / s
            : l === g
                ? 2 + (b - r) / s
                : 4 + (r - g) / s
        : 0;
    return [
        parseInt(60 * h < 0 ? 60 * h + 360 : 60 * h),
        parseInt(100 * (s ? (l <= 0.5 ? s / (2 * l - s) : s / (2 - (2 * l - s))) : 0)),
        parseInt((100 * (2 * l - s)) / 2),
    ];
}

export default { invertHslColor, rgbToHsl, hslToRgb, generateHslColor, generateHslColor_67, hslToStr, autopicker }
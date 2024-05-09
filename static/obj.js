/**
 * @Author: JogFeelingVI
 * @Date:   2024-03-10 20:50:31
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-05-10 00:29:26
 */
"use strict";
import * as obj_funx from "./obj_function.js";

export function pickRandomChars(numChars = 5) {
	// 将字符串转换为数组
	const arr = "aBshiuyRfhklMezx1235670".split("");
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
	return pickedChars.join("");
}

export class swclassforjson {
	// 根据map信息生产新的元素结构体
	constructor(idx = "idx", before = "", after = "", check = false) {
		this.inputidx = `swclass_${pickRandomChars(5)}`;
		this.main = document.getElementById(idx);
		this.before = before;
		this.after = after;
		this.check = check;
		this.makeupEL();
	}

	makeupEL() {
		// 按照图纸制造结构体
		//document.createElement
		let Jsmap = this.makeup_Obj();
		Jsmap.forEach((items) => {
			let reitem = this.makeuped(items);
			if (!Object.is(reitem, null)) {
				this.main.append(reitem);
			}
		});
		console.log(`swclass obg makeup done ${this.inputidx}`);
	}

	get checked() {
		let check = document.getElementById(this.inputidx).checked;
		return check;
	}

	makeup_Obj() {
		let objmap = [
			{
				tag: "main",
				class: "sw",
				child: [
					{
						tag: "label",
						for: "id",
						child: [
							{ tag: "div", class: "qian", append: "before" },
							{
								tag: "div",
								class: "see",
								child: [
									{
										tag: "input",
										type: "checkbox",
										id: "id",
										checked: false,
									},
									{ tag: "div", class: "bg" },
									{ tag: "div", class: "shou" },
								],
							},
							{ tag: "div", class: "hou", append: "after" },
						],
					},
				],
			},
		];
		return objmap;
	}

	makeuped(item = { tag: "div", class: "sw" }) {
		let keys = Object.keys(item);
		if (keys.includes("tag")) {
			if (item["tag"] === "main") {
				this.main.classList.add("sw");
				let itemm = item["child"];
				itemm.forEach((item) => {
					this.main.append(this.makeuped(item));
				});
				return null;
			}

			let el = document.createElement(item["tag"]);

			if (keys.includes("class")) {
				el.classList.add(item["class"]);
			}
			if (keys.includes("for")) {
				el.setAttribute("for", this.inputidx);
			}
			if (keys.includes("id")) {
				el.setAttribute("id", this.inputidx);
			}
			if (keys.includes("append")) {
				let flg = item["append"];
				if (flg === "before") {
					el.innerHTML = this.before;
				}
				if (flg === "after") {
					el.innerHTML = this.after;
				}
			}
			if (keys.includes("type")) {
				el.setAttribute("type", item["type"]);
			}
			if (keys.includes("checked")) {
				if (this.check === true) {
					el.setAttribute("checked", "");
				}
			}
			if (keys.includes("child")) {
				let child = item["child"];
				child.forEach((item_child) => {
					el.append(this.makeuped(item_child));
				});
			}
			return el;
		}
		return null;
	}
	// 生成机构体需要的图纸 json
}

export class radioList {
	constructor(
		idx = "id",
		Comment = "radioList",
		items = [10, 20, 50, 100, 200]
	) {
		this.radioListEL = document.getElementById(idx);
		this.radioListEL.classList.add("radioList");
		this.values = items;
		if (!Object.is(this.radioListEL, null)) {
			if (!Object.is(Comment, null)) {
				this.radioListEL.append(this.init_Comment(Comment));
				this.name = pickRandomChars(5);
				this.items_inx = 0;
				items.forEach((v, i) => {
					let EL = this.init_items(v, i);
					this.radioListEL.append(EL);
				});
			}
		}
	}

	checkItem() {
		let inputs = this.radioListEL.getElementsByTagName("input");
		Array.from(inputs).forEach((v, i) => {
			if (v.checked) {
				return Number(v.getAttribute("value"));
			}
		});
	}

	set setChecked(value = 5) {
		if (!this.values.includes(value)) {
			value = this.values[0];
		}
		let inputs = this.radioListEL.getElementsByTagName("input");
		Array.from(inputs).forEach((v, i) => {
			if (v.getAttribute("value") === `${value}`) {
				v.checked = true;
				return v;
			}
		});
	}

	init_Comment(c = "info") {
		// c = Comment 注释说明
		let comEL = document.createElement("span");
		comEL.innerHTML = c;
		return comEL;
	}

	init_items(i = 5, index = 10) {
		// i shuzhi 5 6 8 9 10 deng
		// <label>
		//     <input name="gs" type="radio" value="15" />
		//     <span>15</span>
		// </label>
		let labelEL = document.createElement("label");
		let input = document.createElement("input");
		let span = document.createElement("show");
		input.classList.add("none");
		input.setAttribute("name", this.name);
		input.setAttribute("type", "radio");
		input.setAttribute("value", i);
		if (index === this.items_inx) {
			input.setAttribute("checked", "");
		}
		span.classList.add("sp");
		span.innerHTML = i;
		labelEL.classList.add("item");
		labelEL.append(input, span);
		return labelEL;
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
	constructor(idx = "id", min = 5, max = 1000, step = 5) {
		this.sliderValue = null;
		this.range = document.getElementById(idx);
		this.range.classList.add("meRange");
		this.range_width = this.range.getBoundingClientRect().width;
		let cls_name = ["huagui_bg", "huagui"];
		if (!Object.is(this.range, null)) {
			cls_name.forEach((v, i, arr) => {
				let temp = this.init_div(v);
				if (v === "huagui_bg") {
					this.attr = this.init_Attributes(min, max, step);
					temp.append(this.attr);
				}
				if (v === "huagui") {
					this.shoubing = this.init_div("shoubing");
					temp.append(this.shoubing);
				}
				this.range.append(temp);
			});
		}
		this.range_max_width =
			this.range_width - this.shoubing.getBoundingClientRect().width;
		this.doStart = (e) => {
			return this.startDrag(e);
		};
		this.doMove = (e) => {
			return this.moveDrag(e);
		};
		this.doEnd = (e) => {
			return this.endDrag(e);
		};
		this.shoubing.addEventListener("mousedown", this.doStart);
	}

	setSRV(idx = "slider-range-value") {
		// 在web app 上显示当前数值
		let srv = document.getElementById(idx);
		if (!Object.is(srv, null)) {
			this.sliderValue = srv;
		} else {
			console.log(`setting SRV done.`);
		}
	}

	echo(val = 25) {
		// 社会元素sliderValue为输出元素
		if (!Object.is(this.sliderValue, null)) {
			this.sliderValue.innerText = val;
		}
	}

	setValue(val = 25) {
		// 启动的时候使用
		this.attr.setAttribute("value", val);
		let left = (val / (this.max - this.min)) * this.range_max_width;
		this.shoubing.style.left = `${left}px`;
		this.shoubing.style.setProperty("--oks", `${left}px`);
		this.shoubing.style.setProperty("--okb", `-${left}px`);
		this.echo(val);
		return val;
	}

	get min() {
		return Number(this.attr.getAttribute("min"));
	}

	get max() {
		return Number(this.attr.getAttribute("max"));
	}

	get value() {
		return Number(this.attr.getAttribute("value"));
	}

	get step() {
		return Number(this.attr.getAttribute("step"));
	}

	shoubing_left(left = 65) {
		this.shoubing.style.left = `${left}px`;
		this.shoubing.style.setProperty("--oks", `${left}px`);
		this.shoubing.style.setProperty("--okb", `-${left}px`);
		let bili =
			(left / this.range_max_width) * (this.max - this.min) + this.min;
		bili = this.roundToStep(bili, this.step);
		this.attr.setAttribute("value", bili);
		this.echo(bili);
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
		let attr = document.createElement("attributes");
		attr.setAttribute("min", min);
		attr.setAttribute("max", max);
		attr.setAttribute("value", min);
		attr.setAttribute("step", step);
		return attr;
	}

	init_div(cls = "huagui_bg") {
		let div = document.createElement("div");
		div.classList.add(cls);
		return div;
	}

	startDrag(event) {
		this.startX = event.clientX;
		// console.log(`startDrag ${event.clientX}`)
		document.addEventListener("mousemove", this.doMove);
		document.addEventListener("mouseup", this.doEnd);
	}

	moveDrag(event) {
		// let getStyle = window.getComputedStyle(this.shoubing);
		// let leftVal = parseInt(getStyle.left) + (event.clientX - this.startX);
		let leftVal = this.shoubing.offsetLeft + (event.clientX - this.startX);
		// console.log(`moveDrag ${leftVal}`)
		if (leftVal >= 0 && leftVal <= this.range_max_width) {
			this.shoubing_left(leftVal);
		}
		this.startX = event.clientX;
	}

	endDrag(event) {
		// console.log(`endDrag ${event}`)
		document.removeEventListener("mousemove", this.doMove);
		document.removeEventListener("mouseup", this.doEnd);
	}
}

export class groupmanage {
	constructor(idx = "idx", size = 5) {
		// init manage
		this.manage = document.getElementById(idx);
		this.manage.classList.add("manage");
		this.group_size = size;
	}

	datasilce(data = {}, size = -1) {
		let _data = {
			1: ["03 04 20 27 28 29", "05"],
			2: ["03 06 20 23 27 29", "05"],
			3: ["03 08 20 25 28 31", "05"],
			4: ["03 19 20 24 27 28", "05"],
			5: ["03 10 19 22 24 29", "05"],
			6: ["03 12 20 22 23 26", "05"],
			9: ["03 11 20 22 23 32", "05"],
			10: ["03 05 08 26 30 33", "05"],
			11: ["03 06 19 21 22 31", "05"],
			13: ["03 10 19 20 29 33", "05"],
			15: ["03 13 20 24 29 32", "05"],
			16: ["03 05 19 26 30 31", "05"],
			17: ["03 05 11 26 27 32", "05"],
			18: ["03 08 11 21 23 26", "05"],
			20: ["03 19 22 25 29 30", "05"],
			22: ["03 19 22 24 28 32", "05"],
			24: ["03 05 25 26 30 33", "05"],
		};
		if (Object.entries(data).length != 0) {
			_data = data;
			console.log(`use groupmanage _data.`);
		} else {
			console.log(`use groupmanage _data is Test.`);
		}
		if (size == -1) {
			size = this.group_size;
		}
		console.log(`setting group size ${size}`);
		this.manage.innerHTML = "";
		let group_index = [];
		for (let i = 0; i < Object.entries(_data).length; i += size) {
			group_index.push(Object.entries(_data).slice(i, i + size));
		}
		console.log(`group slice ${group_index.length}`);
		group_index.forEach((item, index) => {
			this.manage.append(this.maker_group(item, index));
		});
	}

	maker_group(item = [], index = 0) {
		// id = _item[0]
		// 红色号码 = _item[1][0]
		// 蓝色号码 = _item[1][1]
		let group = document.createElement("div");
		let [bgs, fcs] = obj_funx.default.autopicker();
		group.style.setProperty("--bgs", bgs);
		group.style.setProperty("--fcs", fcs);
		group.classList.add("group", "anmin");
		group.innerHTML = `<div class="haed"><span class="a">Group</span> <span class="a">${index}</span></div>`;
		item.forEach((_item, _index, _arr) => {
			let child = `<div><span class="r">${_item[1][0]}</span> <span class="b">${_item[1][1]}</span></div>`;
			if ((_index + 1) % 5 === 0 && _index !== _arr.length - 1) {
				child += `<div class="spb"></div>`;
			}
			group.innerHTML += child;
		});
		return group;
	}
}

// {'list': ['dzx', 'acvalue', 'linma', 'duplicates', 'sixlan', 'lianhao', 'mod2', 'mod3', 'mod4', 'mod5', 'mod6', 'mod7', 'dx16', 'zhihe', 'coldns', 'onesixdiff'], 'checked': ['acvalue', 'linma', 'duplicates', 'sixlan', 'mod2', 'mod3', 'mod4', 'mod5', 'mod6', 'mod7', 'dx16', 'zhihe'], 'status': 'done'}

export class filterList {
	constructor(idx = "filter_group") {
		this.group = document.getElementById(idx);
	}

	initForJson(str = "") {
		if (typeof str != "string" || str.trim() === "") {
			return null;
		} else {
			try {
				let _data = JSON.parse(str);
				this.initForData(_data);
			} catch (error) {
				console.log(`JSON.parse Error`);
			}
		}
	}

	initForData(data = { list: [], checked: [] }) {
		if (data.hasOwnProperty("list") && data.hasOwnProperty("checked")) {
			this.group.innerHTML = "";
			data.list.forEach((item, index, arr) => {
				let check = data.checked.includes(item);
				this.group.append(this.installItem(item, check));
			});
		}
	}

	installItem(name = "xiten", checked = false) {
		let id = pickRandomChars(5);
		let item = document.createElement("div");
		let input = document.createElement("input");
		let label = document.createElement("label");
		input.setAttribute("id", id);
		input.setAttribute("type", "checkbox");
		input.setAttribute("label_name", name);
		if (checked === true) {
			input.setAttribute("checked", "");
		}
		label.setAttribute("for", id);
		label.innerHTML = name;
		item.append(input, label);
		item.classList.add("filterswitch");
		return item;
	}

	getCheckedAll() {
		let data = {};
		const inputs = this.group.getElementsByTagName("input");
		Object.entries(inputs).forEach(([i, item]) => {
			if (item.checked) {
				let name = item.getAttribute("label_name");
				data[name] = true;
			}
		});
		return data;
	}
	// <div class="filterswitch">
	//     <input type="checkbox" id="xd" />
	//     <label for="xd">Adobe XD</label>
	// </div>
}

export class wssocket {
	constructor() {
		this.socket = new WebSocket("ws://192.168.1.159:8080/ws_handle");
		this.open = (e) => {
			return this.onopen(e);
		};
		this.shoudao = (e) => {
			return this.shoudao(e);
		};
		this.close = (e) => {
			return this.onclose(e);
		};
		this.socket.addEventListener("open", this.open);
		this.socket.addEventListener("message", this.shoudao);
		this.socket.addEventListener("close", this.close);
	}

	onopen(event) {
		console.log(`ws handle is open.`);
	}

	shoudao(event) {
		console.log("Message from server ", event.data);
	}

	onclose(event) {
		console.log(`ws handle is claose.`);
	}

	fasong(data = "") {
		this.socket.send(data);
	}
}

// {
// 	"name": "dzx",
// 	"Optional": [
// 		"2:2:2",
// 	],
// 	"recommend": [
// 		"3:1:2",
//
// 	],
// 	"checked": false,
// 	"Description": "d is 23-33, z is 12-22,x is 1-11."
// }

export class filter_all {
	constructor(idx = "filter_group") {
		this.eidx = document.getElementById(idx);
		this.eidx.innerHTML = "";
	}

	getCheckedAll() {
		let temp = {};
		let components = this.getJson("");
		components.forEach((item) => {
			if (item.checked === true) {
				temp[item.name] = true;
			}
		});
		return temp;
	}

	getJson(config = "json") {
		let components = [];

		let componentElements = this.eidx.querySelectorAll(".filter_all");
		componentElements.forEach((item) => {
			let elmap = this.get_name(item);
			components.push(elmap);
		});
		if (config === "json") {
			components = JSON.stringify(components);
		}
		// console.log(JSON.stringify(components));
		return components;
	}

	get_name(e = document.createElement("name")) {
		let name = e.querySelector("label.name");
		let check = name.querySelector("input.use_none").checked;
		let na = name.querySelector("show.NA").textContent;
		let de = name.querySelector("show.DE").textContent;
		let command = e.querySelector("div.command");
		let comd_items = Array.from(command.getElementsByClassName("item"));
		let Op = [];
		let Re = [];
		comd_items.forEach((comd_i) => {
			let sp = comd_i.querySelector("show.sp").textContent;
			let check_none = comd_i.querySelector("input.none").checked;
			Op.push(sp);
			if (check_none === true) {
				Re.push(sp);
			}
			// console.log(sp, check_none);
		});

		return {
			name: na,
			Description: de,
			checked: check,
			Optional: Op,
			recommend: Re,
		};
	}

	initForData(data = { list: [], status: "done" }) {
		// console.log(data)
		data.list.forEach((value, index, arr) => {
			let f_all = document.createElement("div");
			f_all.classList.add("filter_all");
			let name = this.init_Name(
				value.name,
				value.Description,
				value.checked
			);
			let commands = this.init_Command(value.Optional, value.recommend);
			f_all.append(name, commands);
			this.eidx.append(f_all);
		});
	}

	init_Command(Optional = [], recommend = []) {
		let command = document.createElement("div");
		command.classList.add("command");
		Optional.forEach((item, index, arr) => {
			if (recommend.includes(item)) {
				command.append(this.init_Item(item, true));
			} else {
				command.append(this.init_Item(item, false));
			}
		});
		return command;
	}

	init_Item(info = "", check = false) {
		let item = document.createElement("label");
		let none = document.createElement("input");
		let sp = document.createElement("show");
		item.classList.add("item");
		none.classList.add("none");
		none.setAttribute("type", "checkbox");
		if (check === true) {
			none.setAttribute("checked", "");
		}
		sp.classList.add("sp");
		sp.innerText = info;
		item.append(none, sp);
		return item;
	}

	init_Name(Na = "name", De = "", check = false) {
		let nade = document.createElement("label");
		let use_none = document.createElement("input");
		let na = document.createElement("show");
		let de = document.createElement("show");
		nade.classList.add("name");
		use_none.classList.add("use_none");
		use_none.setAttribute("type", "checkbox");
		if (check === true) {
			use_none.setAttribute("checked", "");
		}
		na.classList.add("NA");
		na.innerText = Na;
		de.classList.add("DE");
		de.innerText = De;
		nade.append(use_none, na, de);
		return nade;
	}
}

export class footer {
	constructor(
		idx = "footer",
		config = {
			title: "this web info",
			text: "text",
			links: { google: "www.google.com" },
			Copyright: "© 2024 Copyright JogFeelingVI",
			cr_link: "www.github.com",
			cr_name: "Github",
		}
	) {
		this.footer = document.getElementById(idx);
		this.footer.classList.add("footer");
		this.footer.innerHTML = "";
		let container = this.create_div("container");
		let line_cols = this.create_div("line");
		line_cols.append(this.create_infos(config.title, config.text));
		line_cols.append(this.create_links(config.links));
		let line_Copyright = this.create_Copyright(
			config.Copyright,
			config.cr_link,
			config.cr_name
		);
		container.append(line_cols, line_Copyright);
		this.footer.append(container);
	}

	create_div(class_name = "container") {
		let div = document.createElement("div");
		div.classList.add(class_name);
		return div;
	}

	create_link(name = "", href = "", classname = "toR") {
		let link = document.createElement("a");
		link.setAttribute("href", "https://" + href);
		link.innerText = name;
		link.classList.add("link_a", classname);
		return link;
	}

	create_Copyright(copyright = "this Copyright", link = "", name = "") {
		let line = this.create_div("line");
		let span = document.createElement("span");
		span.innerText = copyright;
		let link_a = this.create_link("* Github *", "www.github.com", "toR");
		line.append(span, link_a);
		return line;
	}

	create_h5(str = "Title") {
		let title = document.createElement("h5");
		title.innerText = str;
		return title;
	}

	create_p(str = "this p element") {
		let text_p = document.createElement("p");
		text_p.innerText = str;
		text_p.classList.add("toDuan");
		return text_p;
	}

	create_infos(title = "", pstr = "") {
		let info = this.create_div("infos");
		info.append(this.create_h5(title), this.create_p(pstr));
		return info;
	}

	create_links(links = { google: "www.google.com" }) {
		let link_all = this.create_div("links");
		let title = this.create_h5("Links");
		link_all.append(title);
		let ui_all = document.createElement("ui");
		let keys = Object.keys(links);
		keys.forEach((k) => {
			console.log(k, links[k]);
			let li_a = document.createElement("li");
			li_a.append(this.create_link(k, links[k], "toLi"));
			ui_all.append(li_a);
		});
		link_all.append(ui_all);
		return link_all;
	}
}

export class fixbutton {
	constructor(
		idx = "footer",
		config = {
			color: "red",
			icon: "science",
			size: "small",
			links: [
				{ color: "red", icon: "tune", click: "", size: "tiny" },
				{
					color: "yellow",
					icon: "done",
					click: "doneClicked()",
					size: "tiny",
				},
				{
					color: "green",
					icon: "download",
					click: "donwLoadGroup()",
					size: "tiny",
				},
				{
					color: "blue",
					icon: "science",
					click: "donwLoadGroup()",
					size: "tiny",
				},
			],
		}
	) {
		this.fixedb = document.getElementById(idx);
		this.fixedb.classList.add("fixtbutton");
		this.fixedb.append(
			this.create_icon(config.color, config.icon, "", config.size)
		);
		this.fixedb.append(this.create_ui(config.links));
	}

	create_ui(links = []) {
		let ui = document.createElement("ui");
		links.forEach((item) => {
			let lix = document.createElement('li')
			lix.append(this.create_icon(item.color, item.icon, item.click, item.size))
			ui.append(lix);
		});
		return ui;
	}

	create_icon(color = "red", icon = "done", click = "", size = "small") {
		let link_a = document.createElement("a");
		if (size === "small") {
			link_a.classList.add("btn", color);
		}else{
			// link_a.setAttribute('style','opacity: 1; transform: scale(0.4) translateY(40px) translateX(0px);')
			link_a.classList.add("btn","btn_s", color);
		}

		let ico = document.createElement("i");
		ico.classList.add("material-icons", size);
		ico.innerText = icon;
		link_a.append(ico);
		if (click.length != 0) {
			link_a.setAttribute("onclick", click);
		}
		return link_a;
	}
}

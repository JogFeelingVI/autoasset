/**
 * @Author: JogFeelingVI
 * @Date:   2024-03-06 15:32:30
 * @Last Modified by:   JogFeelingVI
 * @Last Modified time: 2024-05-09 22:43:26
 */
"use strict";
import * as objJs from "./obj.js";
let rego_user = new objJs.swclassforjson("yesno", "yes", "nx", true);
let rego_v2 = new objJs.swclassforjson("okye", "A", "B", true);
let group_size = new objJs.radioList(
	"GroupSizes",
	"Group Size",
	[10, 20, 30, 50, 100, 200]
);
let ranges = new objJs.meRange("ranges", 5, 1000, 5);
let groupman = new objJs.groupmanage("groupblack", 10);
let filter_group = new objJs.filter_all("filter_group");
// let socket = new objJs.wssocket();
let fixed = new objJs.fixbutton('fixbut')

let footer = new objJs.footer("footerx", {
	title: "Friendly Reminder",
	text: "This is a web app based on PYTHON, which aims to provide simple, intuitive, fast and accurate double-colour ball number generation service. But winning the lottery still depends on your own efforts.",
	links: {
		"google fonts": "fonts.google.com/icons",
		materializecss: "materializecss.com/getting-started.html",
		aioHttp: "demos.aiohttp.org/en/latest/preparations.html",
		Colores: "coolors",
	},
	Copyright: "© 2024 Copyright JogFeelingVI",
	cr_link: "www.github.com",
	cr_name: "Github",
});
//

+(function () {
	console.log("install fixed-action-btn");
	document.addEventListener("DOMContentLoaded", (event) => {
		let acts = document.querySelectorAll(".fixed-action-btn");
		let action = M.FloatingActionButton.init(acts, "");
		/* install modal .modal */
	});
})();

+(function () {
	group_size.setChecked = 300;
	ranges.setSRV("range_value");
	ranges.setValue(35);
	groupman.datasilce();
})();

+(function () {
	fetch("/Detailed_configuration")
		.then((res) => res.json())
		.then((data) => {
			// console.log(data);
			filter_group.initForData(data);
			let retx = filter_group.getCheckedAll();
			console.log(retx);
		});
	// let check = filter_group.getCheckedAll()
	// console.log(check)
})();

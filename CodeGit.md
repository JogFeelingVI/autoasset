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

* Style the label containing the input element */
.container {
  display: block;
  position: relative;
  padding-left: 24px;
  margin-bottom: 12px;
  cursor: pointer;
  user-select: none;
}

/* Hide the browser's default checkbox */
.container input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
  height: 0;
  width: 0;
}
/* Create a custom checkbox */
.checkmark {
  position: absolute;
  top: 0;
  left: 0;
  height: 13px;
  width: 13px;
  background-color: #EAF0F6;
  border: 2px solid #33475B;
  border-radius: 5px;
}

/* When the checkbox is checked, add a navy background */
.container input:checked ~ .checkmark {
  background-color: #33475B;
}

/* Create the checkmark (hidden when not checked) */
.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the checkmark when checked */
.container input:checked ~ .checkmark:after {
  display: block;
}

/* Style the checkmark */
.container .checkmark:after {
  left: 3px;
  width: 4px;
  height: 8px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}
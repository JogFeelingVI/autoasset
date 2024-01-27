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
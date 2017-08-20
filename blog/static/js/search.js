function getSearchResult() {
    var radios = document.getElementsByName("search_criteria");
    var search_result_url;

    var checkedCriteria;
    for (var i = 0, length = radios.length; i<length; i++){
        if (radios[i].checked){
            checkedCriteria = radios[i].value;
        break;
        }
    }

    var search_result_url;
    if (checkedCriteria == "search_by_dpt"){
        search_result_url = "{% url 'post_search_dpt' search_key='NOTAKEY' %}";
    } else {
        search_result_url = "{% url 'post_search_title' search_key='NOTAKEY' %}";
    }

    var search_input = document.getElementById("search_input");

    var result_url = search_result_url.replace('NOTAKEY', search_input.value);
    window.location = result_url;
}

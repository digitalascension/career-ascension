// Function used to search OMNIDB using AJAX.
function searchOMNI(value) {
    var searchTable = document.getElementById("search-table");
    searchTable.innerHTML = '';
    searchTable.innerHTML += "<thead>\n" +
        "                <th>Name</th>\n" +
        "                <th>Created By</th>\n" +
        "                <th>Last Updated</th>\n" +
        "                <th>URL</th>\n" +
        "                <th>Tags</th>\n" +
        "                </thead>";
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var result = JSON.parse(this.responseText);
            searchTable.innerHTML +=
                "<tr>\n" +
                "                        <td><p>" + result[0].Name + "</p></td>\n" +
                "                        <td><p>result.CreatedBy</p></td>\n" +
                "                        <td><p>result.LastUpdated</p></td>\n" +
                "                        <td><p>result.Tags</p></td>\n" +
                "                        <td><p>result.URL</p></td>\n" +
                "                    </tr>"
        }
    };
    xhttp.open("GET", "/search/" + value, true);
    xhttp.send();
}

// Function used to close the OMNI information jumbotron.
function closeInfo() {
    document.getElementById("omni-information").style.display = "none";
}
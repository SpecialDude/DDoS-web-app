let row_count = 1;

function addMoreRow() {
    const form_table = document.getElementById("form-table");

    const table_row = document.createElement("tr");

    const table_head_row = form_table.getElementsByTagName("thead")[0].getElementsByTagName("tr")[0];

    const no_of_features = table_head_row.children.length;
    row_count++;

    for (let i = 0; i < no_of_features - 1; i++)
    {
        let table_data = document.createElement("td");
        let table_input = document.createElement("input");
        table_input.type = "number";
        table_input.name = table_head_row.children[i].innerHTML;
        console.log(table_input.name);

        table_data.appendChild(table_input)

        table_row.appendChild(table_data);
    }

    form_table.getElementsByTagName("tbody")[0].appendChild(table_row);

}

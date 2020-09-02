function struct_json = json_parse(json_file_name)
%{

    Given a string of json file name, this function returns a struct which
    includes the json variables.

    Inputs:
        json_file_name - a string for the json file name

    Outputs:
        sruct_json - a struct which contains the json file values

%}

    fid = fopen(json_file_name);
    raw = fread(fid, inf);
    str = char(raw');
    fclose(fid);
    struct_json = jsondecode(str);
end
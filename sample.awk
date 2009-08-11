BEGIN {
	FS = ","
	fuzzy = 4
}

{
    record_ty = substr($0, 121, 2);
    entity = substr($0, 132, 2);
    if (record_ty == "2D") {
        svc_nm = substr($0, 136, 45);
    }
    if ((record_ty == "4A") && (entity == "PO")) {
        circuit_id = substr($0, 285, 30);
        svc_nm_desc = substr($0, 134, 45);
        print "[" svc_nm_desc "] [" circuit_id "]";
    }
}

END {

}

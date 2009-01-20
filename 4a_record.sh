#!/usr/bin/ksh
## This shell script extracts 2D charges from a given
## Input File which is in the Gateway SIF format.

file_nm=${1}

nawk '{
	record_ty=substr($0,121,2);
	entity=substr($0,132,2);
	if (record_ty == "2D") {
		svc_nm=substr($0,136,45);
	}
	if ((record_ty == "4A") && (entity == "PO")) {
		circuit_id=substr($0,285,30);
		svc_nm_desc=substr($0,134,45);
		print "[" svc_nm_desc "] [" circuit_id "]";
	}
}' ${file_nm}

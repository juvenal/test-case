#!/usr/bin/ksh
## This shell script extracts 2D charges from a given
## Input File which is in the Gateway SIF format.

file_nm=${1}

nawk '{
	record_ty=substr($0,121,2);
	svc_reqst_desc=substr($0,80,20);

	if ((record_ty == "2D") && (svc_reqst_desc == "CONTR LEVEL DISCOUNT")) {
		print $0;
	}
}' ${file_nm}

bool  packet_in ;
int  port ;
int  zcount ;
int  ocount ;
switch(state){
	case 0: {//Goal #0 reached !
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		break;
	}
	case 1: {//Moving towards goal : #3
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		break;
	}
	case 2: {//Moving towards goal : #1
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		break;
	}
	case 3: {//Goal #3 reached !
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		break;
	}
	case 4: {//Moving towards goal : #0
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		break;
	}
	case 5: {//Goal #2 reached !
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		break;
	}
	case 6: {//Moving towards goal : #2
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( ~port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( ~port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		break;
	}
	case 7: {//Goal #1 reached !
		if ( port@0 && ~port@1 && zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && zcount@1 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ~ocount@0 && ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && ~zcount@1 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =1
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && packet_in') {
				port@0 =0
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =1
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( ~packet_in && ~packet_in') {
				zcount@0 =0
				zcount@1 =0
				ocount@1 =0
			}
		}
		if ( port@0 && ~port@1 && ~zcount@0 && zcount@1 && ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =0
				ocount@1 =1
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =0
				ocount@1 =1
			}
		}
		if ( port@0 && ~port@1 && zcount@0 && ~zcount@1 && ~ocount@0 && ~ocount@1) {
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =1
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =1
				ocount@0 =1
				ocount@1 =0
			}
			if ( packet_in && ~packet_in') {
				port@0 =1
				port@1 =0
				zcount@0 =0
				zcount@1 =0
				ocount@0 =1
				ocount@1 =0
			}
		}
		break;
	}
}

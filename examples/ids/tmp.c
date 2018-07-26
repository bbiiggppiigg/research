bool  src_ip_in ;
bool  dst_ip_in ;
bool  packet_in ;
bool  infect ;
bool  src_ip_out ;
bool  dst_ip_out ;
bool  packet_out ;
bool  infected ;
switch(state){
	case 0: {//Goal #0 reached !
		if ( packet_out && infected) {
			if ( src_ip_in && dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =0
				infected =1
			}
			if ( src_ip_in && dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =0
			}
			if ( src_ip_in && dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =0
				infected =1
			}
			if ( src_ip_in && dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =0
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =0
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =0
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =0
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =0
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =0
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =0
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =0
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =0
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =0
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =0
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =0
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =0
			}
		}
		if ( packet_out) {
			if ( src_ip_in && dst_ip_in && ~packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				infected =1
			}
			if ( src_ip_in && dst_ip_in && ~packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
			}
			if ( src_ip_in && dst_ip_in && ~packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
				infected =1
			}
			if ( src_ip_in && dst_ip_in && ~packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
			}
			if ( src_ip_in && ~dst_ip_in && ~packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && ~packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
			}
			if ( src_ip_in && ~dst_ip_in && ~packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && ~packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
			}
			if ( ~src_ip_in && dst_ip_in && ~packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && ~packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
			}
			if ( ~src_ip_in && dst_ip_in && ~packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && ~packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
			}
			if ( ~src_ip_in && ~dst_ip_in && ~packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && ~packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
			}
			if ( ~src_ip_in && ~dst_ip_in && ~packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && ~packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
			}
		}
		if ( packet_out && ~infected) {
			if ( src_ip_in && dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =1
				infected =1
			}
			if ( src_ip_in && dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =1
			}
			if ( src_ip_in && dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =1
				infected =1
			}
			if ( src_ip_in && dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =1
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =1
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =1
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =1
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =1
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =1
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =1
			}
		}
		break;
	}
	case 1: {//Moving towards goal : #0
		if ( ~packet_out) {
			if ( src_ip_in && dst_ip_in && ~packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =1
				infected =1
			}
			if ( src_ip_in && dst_ip_in && ~packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =1
			}
			if ( src_ip_in && dst_ip_in && ~packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
				infected =1
			}
			if ( src_ip_in && dst_ip_in && ~packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
			}
			if ( src_ip_in && ~dst_ip_in && ~packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =1
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && ~packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =1
			}
			if ( src_ip_in && ~dst_ip_in && ~packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && ~packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
			}
			if ( ~src_ip_in && dst_ip_in && ~packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =1
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && ~packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =1
			}
			if ( ~src_ip_in && dst_ip_in && ~packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && ~packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
			}
			if ( ~src_ip_in && ~dst_ip_in && ~packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =1
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && ~packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =1
			}
			if ( ~src_ip_in && ~dst_ip_in && ~packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && ~packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
			}
		}
		if ( ~packet_out && ~infected) {
			if ( src_ip_in && dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =1
				infected =1
			}
			if ( src_ip_in && dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =1
			}
			if ( src_ip_in && dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =1
				infected =1
			}
			if ( src_ip_in && dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =1
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =1
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =1
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =1
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =1
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =1
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =1
			}
		}
		if ( ~packet_out && infected) {
			if ( src_ip_in && dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =0
				infected =1
			}
			if ( src_ip_in && dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =0
				infected =0
			}
			if ( src_ip_in && dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =0
				infected =1
			}
			if ( src_ip_in && dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =1
				packet_out =0
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =0
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =0
				infected =0
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =0
				infected =1
			}
			if ( src_ip_in && ~dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =1
				dst_ip_out =0
				packet_out =0
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =0
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =0
				infected =0
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =0
				infected =1
			}
			if ( ~src_ip_in && dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =1
				packet_out =0
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =0
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && ~infect && packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =0
				infected =0
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =0
				infected =1
			}
			if ( ~src_ip_in && ~dst_ip_in && packet_in && ~infect && ~packet_in') {
				src_ip_out =0
				dst_ip_out =0
				packet_out =0
			}
		}
		break;
	}
}

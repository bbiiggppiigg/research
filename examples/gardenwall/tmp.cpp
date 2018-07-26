#define MAX_GOAL 1

int state; 
int goal = 0;
int src_ip_in, src_ip_in_primed; 
int dst_ip_in, dst_ip_in_primed; 
bool packet_in , packet_in_primed ;
bool infect , infect_primed ;
int src_ip_out  ;
int dst_ip_out  ;
bool packet_out  ;
bool infected  ;
 int main() { 
infect = 0;
infected = 0;
switch(state){
	case 0: {
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && !packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out &= (~(1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && !infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && !infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && !infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in | ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out |= ( (1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in | ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out |= ( (1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				 dst_ip_out |= ( (1 << 0 ));
				 dst_ip_out |= ( (1 << 1 ));
				packet_out =1;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !packet_in_primed && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && !infect_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed & ~(1 << 0 )) &&  ( src_ip_in_primed & ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
		if (  ( src_ip_in & ~(1 << 0 )) &&  ( src_ip_in & ~(1 << 1 )) && packet_in && infect && !packet_out && infected &&  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
			if (  ( src_ip_in_primed | ~(1 << 0 )) &&  ( src_ip_in_primed | ~(1 << 1 )) && packet_in_primed) {
				 src_ip_out &= (~(1 << 0 ));
				 src_ip_out &= (~(1 << 1 ));
				packet_out =0;
				infected =1;
				break;
			}
		}
}
}
return 0;
}

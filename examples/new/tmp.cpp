#define MAX_GOAL 4

int state; 
int goal = 0;
bool packet_in , packet_in_primed ;
int port  ;
int zcount  ;
int ocount  ;
 int main() { 
packet_in = 1;
zcount=0;
ocount=0;
switch(state){
	case 0: {
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount &= (~(1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount &= (~(1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount &= (~(1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount &= (~(1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount &= (~(1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount &= (~(1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount &= (~(1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				break;
			}
		}
}
	case 1: {
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
}
	case 2: {
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port &= (~(1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
}
	case 3: {
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				goal = ( goal + 1 ) % MAX_GOAL ;
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port | ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount | ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 1 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount &= (~(1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount &= (~(1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) &&  ( ocount & ~(1 << 1 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port &= (~(1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount &= (~(1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( packet_in &&  ( port & ~(1 << 0 )) &&  ( port & ~(1 << 1 )) &&  ( zcount & ~(1 << 0 )) &&  ( zcount | ~(1 << 1 )) &&  ( ocount | ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 0 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && !packet_in_primed) {
			if ( !packet_in_primed) {
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
		if ( !packet_in &&  ( port & ~(1 << 0 )) &&  ( port | ~(1 << 1 )) &&  ( zcount | ~(1 << 0 )) &&  ( zcount & ~(1 << 1 )) &&  ( ocount & ~(1 << 0 )) && packet_in_primed) {
			if ( packet_in_primed) {
				 port |= ( (1 << 0 ));
				 port |= ( (1 << 1 ));
				 zcount |= ( (1 << 0 ));
				 zcount |= ( (1 << 1 ));
				 ocount |= ( (1 << 1 ));
				break;
			}
		}
}
}
return 0;
}

#include <stdio.h>

int main() {
    int coin_num, value_num;
    int count = 0;
    int check = 0;
    
	printf("동전갯수와 만들 가격을 정해주세요\n");
	scanf("%d %d", &coin_num, &value_num);
	int coin[coin_num];
	printf("동전 갯수만큼 동전종류를 입력해주세요\n");
	
	for(int i=0; i<coin_num; i++){
	   scanf("%d", &coin[i]);
	}
	
	for(int j=0; j<coin_num; j++){
	    if(value_num<coin[j+1]){
	        value_num = value_num - coin[j];
	        count = count+1;
	        if(value_num == 0){
	            printf("최소 갯수 : %d", count);
	            break;
	        }
	        j=0;
	        continue;
	    }
	}
	return 0;
}

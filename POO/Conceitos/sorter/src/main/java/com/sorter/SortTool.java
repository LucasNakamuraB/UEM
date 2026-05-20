package com.sorter;

public class SortTool {
    
    public void sort(Vector vector){
        for (int i = 0; i < vector.getSize(); i++){
            for (int n = 0; n < vector.getSize() -1; n++){
                if (vector.get(n) > vector.get(n + 1)){
                    vector.index_switch(n, n+1);
                }
            }
        }

    }
}

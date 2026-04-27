package com.sorter;

public class Vector {
    private float[] vector;
    
    public int getSize(){
        return vector.length;
    }
    public float[] getVecotr(){
        return vector;
    }
    public float get(int index){
        return vector[index];
    }

    public void setVector(float[] vector){
        this.vector = vector;
    }

    public void index_switch(int idx1, int idx2){
        float cache = vector[idx1];
        vector[idx1] = vector[idx2];
        vector[idx2] = cache;
    }
}

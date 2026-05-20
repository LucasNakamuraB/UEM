package com.sorter;

public class Main {
    public static void main(String[] args) {
        SortTool sorter = new SortTool();
        Vector vec = new Vector();
        float[] buxa = {2, 5, 1, 8, 3};
        vec.setVector(buxa);
        sorter.sort(vec);
        for (int i = 0; i < vec.getSize(); i++){
            System.out.print(vec.get(i));
        }
    }
}
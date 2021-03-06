package com.tetromino.game;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Random;

/**
 * Created by andre on 3/18/17.
 */
public class Tetromino {
    private final LinkedHashMap<String, List<int[][]>> tetrominos;

    private int row;
    private int col;
    private int rotation;

    private String key;

    public final Texture i_block;
    public final Texture o_block;
    public final Texture t_block;
    public final Texture j_block;
    public final Texture l_block;
    public final Texture s_block;
    public final Texture z_block;

    public Tetromino() {
        row = 0;
        col = 3;
        ArrayList<int[][]> i = new ArrayList<>();
        i.add(new int[][]{
                {0, 1, 0, 0},
                {0, 1, 0, 0},
                {0, 1, 0, 0},
                {0, 1, 0, 0},
        });
        i.add(new int[][]{
                {0, 0, 0, 0},
                {0, 0, 0, 0},
                {1, 1, 1, 1},
                {0, 0, 0, 0},
        });

        ArrayList<int[][]> o = new ArrayList<>();
        o.add(new int[][]{
                {0, 0, 0, 0},
                {0, 2, 2, 0},
                {0, 2, 2, 0},
                {0, 0, 0, 0},
        });

        ArrayList<int[][]> t = new ArrayList<>();
        t.add(new int[][]{
                {0, 0, 0},
                {3, 3, 3},
                {0, 3, 0},

        });
        t.add(new int[][]{
                {0, 3, 0},
                {0, 3, 3},
                {0, 3, 0},

        });
        t.add(new int[][]{
                {0, 3, 0},
                {3, 3, 3},
                {0, 0, 0},
        });
        t.add(new int[][]{
                {0, 3, 0},
                {3, 3, 0},
                {0, 3, 0},
        });

        ArrayList<int[][]> j = new ArrayList<>();
        j.add(new int[][]{
                {0, 0, 0},
                {4, 4, 4},
                {0, 0, 4},
        });
        j.add(new int[][]{
                {0, 4, 4},
                {0, 4, 0},
                {0, 4, 0}
        });
        j.add(new int[][]{
                {4, 0, 0},
                {4, 4, 4},
                {0, 0, 0}
        });
        j.add(new int[][]{
                {0, 4, 0},
                {0, 4, 0},
                {4, 4, 0},
        });
        ArrayList<int[][]> l = new ArrayList<>();

        l.add(new int[][]{
                {0, 0, 0},
                {5, 5, 5},
                {5, 0, 0},
        });
        l.add(new int[][]{
                {0, 5, 0},
                {0, 5, 0},
                {0, 5, 5},
        });
        l.add(new int[][]{
                {0, 0, 5},
                {5, 5, 5},
                {0, 0, 0},
        });
        l.add(new int[][]{
                {5, 5, 0},
                {0, 5, 0},
                {0, 5, 0},
        });

        ArrayList<int[][]> s = new ArrayList<>();
        s.add(new int[][]{
                {0, 0, 0},
                {0, 6, 6},
                {6, 6, 0},
        });
        s.add(new int[][]{
                {0, 6, 0},
                {0, 6, 6},
                {0, 0, 6},
        });

        ArrayList<int[][]> z = new ArrayList<>();
        z.add(new int[][]{
                {0, 0, 0},
                {7, 7, 0},
                {0, 7, 7},
        });
        z.add(new int[][]{
                {0, 0, 7},
                {0, 7, 7},
                {0, 7, 0},
        });

        tetrominos = new LinkedHashMap<>();
        tetrominos.put("i", i);
        tetrominos.put("o", o);
        tetrominos.put("t", t);
        tetrominos.put("j", j);
        tetrominos.put("l", l);
        tetrominos.put("s", s);
        tetrominos.put("z", z);

        key = "";

        Random r = new Random();

        String alphabet = "iotjlsz";

        for (int h = 0; h < 1; h++) {
            key = alphabet.charAt(r.nextInt(alphabet.length())) + "";
        }

        i_block = new Texture(Gdx.files.internal("i_block.png"));
        o_block = new Texture(Gdx.files.internal("o_block.png"));
        t_block = new Texture(Gdx.files.internal("t_block.png"));
        j_block = new Texture(Gdx.files.internal("j_block.png"));
        l_block = new Texture(Gdx.files.internal("l_block.png"));
        s_block = new Texture(Gdx.files.internal("s_block.png"));
        z_block = new Texture(Gdx.files.internal("z_block.png"));

    }

    public int[][] getShape() {
        if (rotation >= tetrominos.get(key).size()) {
            rotation = 0;
        }
        return tetrominos.get(key).get(rotation);
    }

    public void rotateShape() {
        rotation++;
    }

    public void increaseRow() {
        row++;
    }

    public void increaseCol() {
        col++;
    }

    public void decreaseCol() {
        col--;
    }

    public int getRow() {
        return row;
    }

    public int getCol() {
        return col;
    }

}
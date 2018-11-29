package org.luapp;

import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Scalar;
import org.opencv.highgui.HighGui;
import org.opencv.imgcodecs.Imgcodecs;

import java.util.Vector;

/**
 * Hello world!
 */
public class App {
    public static void loadOpenCVNativeLibrary() {
        nu.pattern.OpenCV.loadShared();
    }

    static {
        App.loadOpenCVNativeLibrary();
    }

    public static void test() {
        System.out.println("Welcome to OpenCV " + Core.VERSION);
        Mat m = new Mat(5, 10, CvType.CV_8UC1, new Scalar(0));
        System.out.println("OpenCV Mat: " + m);

        Mat mr1 = m.row(1);
        mr1.setTo(new Scalar(1));

        Mat mc5 = m.col(5);
        mc5.setTo(new Scalar(5));

        System.out.println("OpenCV Mat data:\n" + m.dump());
    }

    public static void readHuidu() {
        String imgPath = "D:\\testpic\\plate1.jpg";
        Mat src = Imgcodecs.imread(imgPath);
        String ret = plateRecognize(src);
    }

    private static String plateRecognize(Mat src) {
        Vector<Mat> matVector= new Vector<Mat>();
        return null;
    }

    public static void main(String[] args) {
        System.out.println("Hello World!");
        test();
    }
}

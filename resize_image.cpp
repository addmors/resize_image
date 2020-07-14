#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include<windows.h>
#include <string>
#include <iostream>
using namespace cv;
using namespace std;

int main()
{
	setlocale(LC_ALL, "ru");
	double a =1; 
	string s= "";
	cout << "Введите коэффициент маштабирования";
	cin >> a;
	cout << "Ведите путь до картинки";
	cin >> s;
	
	Mat image = imread(s, CV_LOAD_IMAGE_COLOR);
	if (image.empty()) {
		cout << "Ошибка ввода файла";
		Sleep(5000);
		return -1;
	}
	cv::resize(image, image, Size(), a, a, 1);
	imwrite("new_image.jpg", image);
	imshow("image", image);
	int key = (waitKey(0) & 0xFF);
	cout << "Успешно!!!";

}
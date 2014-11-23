#include "iostream.h"
int main()
{
   int mark;
   cout <<"请输入成绩（0~100）： ";
   cin >>mark;
   switch(mark/20)
   {
      case 5:
      {
         if (mark>100)//100到119的情况都是mark/20==5，所以要用if语句再次过滤
         {
            cout <<"ERROR!" <<endl;
            break;
         }
      }
      case 4:
      {
         cout <<"Good!" <<endl;
         break;
      }
      case 3:
      {
         cout <<"Soso" <<endl;
         break;
      }
      case 2://根据前面试一试的结论，如果case没有对应的break，会运行到下一个case中
      case 1:
      case 0:
      {
         if (mark>=0)//同样要用if过滤负数
         {
            cout <<"Please work harder!" <<endl;
            break;
         }
      }
      default://其它情况都是出错
      cout <<"ERROR!" <<endl;
   }
   return 0;
}

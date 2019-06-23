package com.yzeng.vm;

/*
 * Saturn Timer
 * 2x faster timer hh:mm:ss, tick every 500ms
 */

import java.lang.Math; // headers MUST be above the first class
import java.util.TimerTask;
import java.util.Date;
import java.lang.Thread;
import java.util.Timer;

// one class needs to have a main() method
public class SaturnTimer
{

  public static void givenUsingTimer_whenSchedulingTaskOnce_thenCorrect() {
      TimerTask task = new TimerTask() {
          public void run() {
              System.out.println("Task performed on: " + new Date() + "\n" +
                "Thread's name: " + Thread.currentThread().getName());
          }
      };
      Timer timer = new Timer("Timer");

      long delay = 1000L;
      timer.schedule(task, delay);
  }
  
  public static void timer() {
	  TimerTask repTask=new TimerTask() {
		private int hh=23, mm=59, ss=50;
		@Override
		public void run() {
			ss++;
			if(ss==60){
				ss=0;
				mm++;
				if(mm==60) {
					mm=0;
					hh++;
					if(hh==24) hh=0;
				}
			}
			// TODO Auto-generated method stub
			String hString = String.format("%02d", hh), 
				mString = String.format("%02d", mm), 
				sString = String.format("%02d", ss);	
			System.out.print(hString+":"+mString+":"+sString+"\r");
		}
	  };
	  Timer timer=new Timer();
	  long delay=500L;
	  long period=500L;
	  timer.scheduleAtFixedRate(repTask, delay, period);
  }
  
  // arguments are passed using the text field below this editor
  public static void main(String[] args)
  {
    timer();
  }
}
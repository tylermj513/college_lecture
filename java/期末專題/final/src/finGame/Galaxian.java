package finGame;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;
import javax.swing.*;

	
public class Galaxian {
	private JFrame frm;
	private JPanel base;
	private JPanel options;//選擇難度、開始界面
	private JPanel game;//進入遊戲的界面
	private JPanel playing;//遊戲界面下面的黑色底色部分，就是戰鬥進行區域
	private CardLayout layers;//在base這個JPanel上設置的Card Layout

	private enum level {//遊戲難度設定
		Easy, Medium, Difficult
	};

	//初始難度設為Easy，各個數據按照此難度初始化
	private level currentLevel = level.Easy;//初始難度
	private int score = 0;//初始得分
	private int lifes = 3;//初始生命

	private JLabel scoreLabel = new JLabel();//顯示得分情況
	private JLabel lifeLabel = new JLabel();//顯示剩餘生命

	private FlyingObj hero;//玩家控制的痞老闆
	
	private boolean running;//表示遊戲進行中
	
	private long lastShoot;//為了控制皮老闆的子彈頻率							
	
	private long lastplane;//為了控制敵人的出現频率，控制敵人出現的時間
							//現在的時間-上次的時間到達一定數值了以後才會出下一個敵人
	
	private long buffstart = 0;//為了控制增益的持續時間，倒計時得增益效果的時間
								//現在的時間-上次的時間到達一定數值了以後取消增益效果
	
	private long lastdeath;//為了設置皮老闆復活後1.5秒的無敵狀態
	
	//子彈數據
	class bullet
	{
		public double x, y;//子彈坐標
		public double xt, yt;//子彈坐標
		public bullet(double x, double y, double xt, double yt) {
			this.x = x;
			this.y = y;
			this.xt = xt;
			this.yt = yt;
		}
	}
	
	private int origss = 750;//沒有增益效果的射速
	private int curss = 750;
	private int enemyfreq = 2000;//敵人出現頻率
	private int enemyb = 8;//蟹老闆子彈
	
	private ArrayList<bullet> bul = new ArrayList<bullet>();//hero敵人射出的子彈
	private ArrayList<bullet> enemybul = new ArrayList<bullet>();//敵人射出的子彈
	private ArrayList<FlyingObj> alive = new ArrayList<FlyingObj>();//出現在場上的敵人 & 增益
	private FlyingObj[] t1 = null;//所有可能出現的海绵寶寶敵方敵人
	private FlyingObj[] t2 = null;//所有可能出現的派大星敵方敵人
	private FlyingObj[] boss = null;//所有可能出現的蟹老闆
	private FlyingObj[] buffs = null;//所有可能出現的增益效果
	
	private int t1lim = 10, t1num = 10;
	private int t2lim = 30, t2num = 30;
	private int bosslim = 0, bossnum = 0;
	private int bufflim = 3, buffnum = 3;
	
	private Timer timer;//控制皮老闆的移動
	private Timer ti2;//控制子彈的移動
	private Timer out;//控制敵人的出現
	private Timer emove;//控制敵人的移動
	private Timer bt;//控制增益效果的出現、增益效果持續時間、皮老闆的出現
	private Timer bossbullet;//控制皮老闆發射子彈
	private Timer checkv;//檢查勝利或失敗
	
	private JLabel r;
	
	@SuppressWarnings({ "static-access", "unchecked", "rawtypes", "serial" })
	public Galaxian() {

		frm = new JFrame("Galaxian");
		base = new JPanel();
		options = new JPanel();
		game = new JPanel();
		playing = new JPanel() {
			public void paint(Graphics g) {
				
				super.paint(g);
				g.setColor(Color.WHITE);
				ArrayList<Integer> tbd = new ArrayList<Integer>();
				ArrayList<Integer> etbd = new ArrayList<Integer>();
				
				//更新我方子彈分數
				for(int i = 0; i < bul.size(); ++i) {
					double rx = bul.get(i).x;
					double ry = bul.get(i).y;
					//子彈對應的(xt,yt)的方向移動
					bul.set(i, new bullet(rx + bul.get(i).xt, ry + bul.get(i).yt, 0, -1));
					g.fillOval((int)(rx), (int)(ry), 10, 10);
					if(ry<0)etbd.add(i);//如果出界則刪除
				}
				
				//更新敵人
				g.setColor(Color.CYAN);
				for(int i = 0; i < enemybul.size(); ++i) {
					double rx = enemybul.get(i).x;
					double ry = enemybul.get(i).y;
					if (rx<=0||rx+10 >= 775||ry>=890) tbd.add(i);//如果出界則刪除
					enemybul.set(i, new bullet(rx + enemybul.get(i).xt, ry + enemybul.get(i).yt, enemybul.get(i).xt, enemybul.get(i).yt));
					g.fillOval((int)(rx), (int)(ry), 10, 10);
				}
				
				//刪除
				for(int i = 0; i < etbd.size(); ++i) {
					bul.remove(etbd.get(i).intValue());
				}
				for(int i = 0; i < tbd.size(); ++i) {
					enemybul.remove(tbd.get(i).intValue());
				}
				
			}
		};
		layers = new CardLayout();
		running = false;
		frm.setResizable(false);
		frm.setDefaultCloseOperation(frm.EXIT_ON_CLOSE);
		frm.setSize(new Dimension(800, 1000));

		base.setLayout(layers);
		//給base設置Card Layout

		JButton start = new JButton("Start");//start按鈕是初始化+遊戲開始
		
		start.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {//進行初始化
				buffnum = bufflim = 3;//一場遊戲最多三個buff
				curss = origss;
				t1num = t1lim;
				t2num = t2lim;
				bossnum = bosslim;
				lifes = 3;
				lifeLabel.setText("   Life: " + lifes + " ");
				score = 0;
				scoreLabel.setText("  Score: " + score);
				layers.next(base);
				running = true;//遊戲開始
				r.setVisible(false);
				if (t1!=null) {
					for(int i = 0; i<20; ++i) {
						t1[i].setVisible(true);
						t1[i].setBackground(Color.WHITE);
						t1[i].setLocation((int)(Math.random()*765), -30);
						t1[i].hp = t1[i].hpLimit;
					}
				}
				if (t1!=null) {
					for(int i = 0; i<50; ++i) {
						t2[i].setVisible(true);
						t2[i].setLocation((int)(Math.random()*765), -30);
						t2[i].hp = t2[i].hpLimit;
					}
				}
				if(buffs!=null) {
					for(int i = 0; i<3; ++i) {
						buffs[i].setVisible(true);
						buffs[i].setLocation((int)(Math.random()*765), -30);
					}
				}
				hero.setLocation(380,820);
				alive.clear();
				bul.clear();
				enemybul.clear();//初始化結束
			}
		});
		
		
		//設置開始面板
		start.setBackground(Color.LIGHT_GRAY);
		start.setPreferredSize(new Dimension(200, 50));
		start.setFont(new Font("courier new", Font.BOLD, 32));

		JPanel up = new JPanel();// title
		JPanel mid = new JPanel();// button
		JPanel down = new JPanel();// selection
		up.setPreferredSize(new Dimension(800, 300));
		mid.setPreferredSize(new Dimension(800, 100));
		down.setPreferredSize(new Dimension(800, 100));

		
		up.setBackground(Color.GRAY);
		mid.setBackground(Color.GRAY);
		down.setBackground(Color.GRAY);

		JLabel text = new JLabel();
		text.setFont(new Font("courier new", Font.BOLD, 56));
		text.setText("Galaxian");
		JPanel blank = new JPanel();
		blank.setPreferredSize(new Dimension(800, 50));
		blank.setBackground(Color.GRAY);
		up.add(blank);
		up.add(text);

		JComboBox comboBox = new JComboBox();
		comboBox.setFont(new Font("courier new", Font.PLAIN, 28));
		comboBox.addItem("Easy");
		comboBox.addItem("Medium");
		comboBox.addItem("Difficult");
		comboBox.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JComboBox s = (JComboBox) e.getSource();
				if (s.getSelectedItem().equals("Easy")) {//各個難度下各種敵人的數量
					currentLevel = level.Easy;
					enemyfreq = 2000;
					t1lim = t1num = 10;
					t2lim = t2num = 30;
					bosslim = bossnum = 0;
				} else if (s.getSelectedItem().equals("Medium")) {
					enemyfreq = 1500;
					currentLevel = level.Medium;
					t1lim = t1num = 15;
					t2lim = t2num = 40;
					bosslim = bossnum = 1;
				} else if (s.getSelectedItem().equals("Difficult")) {
					enemyfreq = 1300;
					currentLevel = level.Difficult;
					t1lim = t1num = 20;
					t2lim = t2num = 50;
					bosslim = bossnum = 2;
				}
			}
		});
		down.add(comboBox);
		
		options.setLayout(new FlowLayout());
		mid.add(start, BorderLayout.CENTER);
		options.add(up);
		options.add(mid);
		options.add(down);

		//設置game
		
		JPanel imf = new JPanel();//最上方的灰色底色橫條，有分數、生命信息和返回、暫停按鈕
		JButton back = new JButton();
		JButton pause = new JButton();
		scoreLabel = new JLabel();
		lifeLabel = new JLabel();

		imf.setPreferredSize(new Dimension(800, 60));
		back.setFont(new Font("courier new", Font.PLAIN, 28));
		back.setText("<= Quit");
		back.setBackground(Color.LIGHT_GRAY);
		back.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				layers.previous(base);//按下back按鈕，就會回到初始面板
				running = false;
			}
		});

		pause.setFont(new Font("courier new", Font.PLAIN, 28));
		pause.setText("Pause");
		pause.setBackground(Color.LIGHT_GRAY);
		pause.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {//按下按鈕後，按鈕上的內容會變為restart，同時遊戲暫停
				JButton s = (JButton) e.getSource();
				if (e.getActionCommand().equals("Pause")) {
					s.setText("Restart");
					running = false;//所有的timer都有if(running)這個條件，所以所有的更新都會停止
				} else if (e.getActionCommand().equals("Restart")) {
					running = true;
					s.setText("Pause");
				}
			}
		});

		scoreLabel.setFont(new Font("courier new", Font.BOLD, 28));
		scoreLabel.setBackground(Color.DARK_GRAY);
		scoreLabel.setText("  Score: " + score);
		scoreLabel.setForeground(Color.WHITE);

		lifeLabel.setFont(new Font("courier new", Font.BOLD, 28));
		lifeLabel.setBackground(Color.DARK_GRAY);
		lifeLabel.setText("   Life: " + lifes + " ");
		lifeLabel.setForeground(Color.WHITE);

		r = new JLabel();
		r.setFont(new Font("courier new", Font.BOLD, 48));
		r.setForeground(Color.WHITE);
		r.setBounds(0,0,400,600);
		playing.add(r);
		r.setVisible(false);
		
		imf.add(back);
		imf.add(scoreLabel);
		imf.add(lifeLabel);
		imf.add(pause);
		imf.setBackground(Color.DARK_GRAY);

		//遊戲面板

		
		playing.setBackground(Color.BLACK);
		playing.setPreferredSize(new Dimension(785, 890));

		playing.setLayout(null);
		
		//戲開始後根據遊戲難度放出對應的敵人數量
		t1 = new FlyingObj[20];
		for(int i = 0; i<20; ++i) {
			t1[i] = new FlyingObj("Enemy,T1", 2);
			
			t1[i].setBounds((int)(Math.random()*765), -30, 30, 30);
			playing.add(t1[i]);
		}
		t2 = new FlyingObj[50];
		for(int i = 0; i<50; ++i) {
			t2[i] = new FlyingObj("Enemy,T2", 1);
			t2[i].setBounds((int)(Math.random()*765), -30, 30, 30);
			playing.add(t2[i]);
		}
		buffs = new FlyingObj[3];
		for(int i = 0; i<3; ++i) {
			buffs[i] = new FlyingObj("Buff", 1);
			buffs[i].setBounds((int)(Math.random()*765), -30, 30, 30);
			playing.add(buffs[i]);
		}
		
		boss = new FlyingObj[2];
		for(int i = 0; i<2; ++i) {
			boss[i] = new FlyingObj("Boss", 20);
			boss[i].setBounds((int)(Math.random()*765), -100, 100, 100);
			playing.add(boss[i]);
		}
		
		
		hero = new FlyingObj("Self", 3);
		hero.setBounds(380, 820, 50, 50);
		playing.add(hero);
		
		game.add(imf);
		game.add(playing);
		
		lastShoot = System.currentTimeMillis();
	 
		frm.setFocusable(true);
		frm.addKeyListener(new KeyListener() {
			@Override
			public void keyPressed(KeyEvent e) {
				switch (e.getKeyCode()) {
				case KeyEvent.VK_LEFT:
					hero.left = true;
					break;
				case KeyEvent.VK_RIGHT:
					hero.right = true;
					break;
				case KeyEvent.VK_UP:
					hero.up = true;
					break;
				case KeyEvent.VK_DOWN:
					hero.down = true;
					break;
				case KeyEvent.VK_SPACE://按空格發射子彈
					scoreLabel.setText("  Score: " + score);
					if(System.currentTimeMillis()-lastShoot>=curss) {
						if(curss == origss) --score;//沒有增益的情況下，子彈會花費一點分數
						bul.add(new bullet(hero.getX()+hero.getWidth()/2, hero.getY(), 0, -1));
						lastShoot = System.currentTimeMillis();
					}
					break;
				}
			}

			@Override
			public void keyReleased(KeyEvent e) {
				switch (e.getKeyCode()) {
				case KeyEvent.VK_LEFT:
					hero.left = false;
					break;
				case KeyEvent.VK_RIGHT:
					hero.right = false;
					break;
				case KeyEvent.VK_UP:
					hero.up = false;
					break;
				case KeyEvent.VK_DOWN:
					hero.down = false;
					break;
				}
			}

			@Override
			public void keyTyped(KeyEvent e) {}
		});
		game.setBackground(Color.BLACK);
		options.setBackground(Color.GRAY);
		

		//移動問題
		
		
		timer = new Timer(); 
		timer.schedule(new TimerTask() { 
			@Override 
			public void run() { 
				if (running) { 
					hero.move();
				}
			} },30, 30);
		
		
		ti2 = new Timer(); 
		ti2.schedule(new TimerTask() { 
			@Override 
			public void run() {
				if (running) { 
					playing.repaint();
				}
			}
		},5, 5);
		
		lastplane = System.currentTimeMillis();
		
		out = new Timer(); 
		out.schedule(new TimerTask() { 
			@Override 
			public void run() {//不同的難度都按一定的速率放出敵人
				if (running) { //如果難度是Medium或者Difficult就有可能斜方向出現敵人
					if(System.currentTimeMillis()-lastplane>=enemyfreq) {
						lastplane = System.currentTimeMillis();
						if (t2num > 0) {
							if(currentLevel == level.Medium) {
								t2[t2lim-t2num].setdirection((int)(Math.random()*3)-1, 1);
							} else if(currentLevel == level.Difficult) {
								t2[t2lim-t2num].setdirection((int)(Math.random()*5)-3, 1);
							}
							alive.add(t2[t2lim-t2num]);
							--t2num;
						} else if(t1num > 0) {
							if(currentLevel == level.Medium) {
								t1[t1lim-t1num].setdirection((int)(Math.random()*3)-1, 1);
							} else if(currentLevel == level.Difficult) {
								t1[t1lim-t1num].setdirection((int)(Math.random()*5)-3, 1);
							}
							alive.add(t1[t1lim-t1num]);
							--t1num;
						}
					}
				}
			}
		},5, 5);
		
		
		
		emove = new Timer(); 
		emove.schedule(new TimerTask() { 
			@Override 
			public void run() {
				if (running) { 
					ArrayList<Integer> tbr = new ArrayList<Integer>();
					ArrayList<Integer> atbr = new ArrayList<Integer>();
					for(int i = 0; i < alive.size(); ++i) {
						double x = alive.get(i).x + alive.get(i).xt;
						double y = alive.get(i).y + alive.get(i).yt;
						alive.get(i).setLocation((int)x,(int)y);
						
						//碰到邊緣回來
						if (x<=0) alive.get(i).setdirection(Math.abs(alive.get(i).xt), alive.get(i).yt);
						else if(x+alive.get(i).getWidth()>=785) alive.get(i).setdirection(-Math.abs(alive.get(i).xt), alive.get(i).yt);
						if (y>=890) atbr.add(i);
						
						//如果是皮老闆會在一定的高度停止向下移動，而改為左右移動
						if (alive.get(i).type.equals("Boss") && y >= 100) {
							alive.get(i).yt = 0;
							if (alive.get(i).x <= 100)
								alive.get(i).xt = Math.abs(alive.get(i).xt);
							else if (alive.get(i).x >= 550)
								alive.get(i).xt = -Math.abs(alive.get(i).xt);
						}
						
						
						//只要撞到的不是增益效果，撞到皮老闆發射的子彈使得會hp減1
						if(!alive.get(i).type.equals("Buff")) {
							for(int j = 0;j<bul.size();++j) {
								double bx = bul.get(j).x;
								double by = bul.get(j).y + 1;
								
								if(bx>=x-5 && bx<=x+alive.get(i).getWidth()-5 && by>=y-0 && by<=y+alive.get(i).getWidth()) {
									tbr.add(j);
									--alive.get(i).hp;
									if(alive.get(i).hp <= 0) {
										alive.get(i).setVisible(false);
										atbr.add(i);
										//得分
										if (alive.get(i).type.equals("Enemy,T2")) score += 10;
										else if (alive.get(i).type.equals("Enemy,T1")) score += 15;
										else if (alive.get(i).type.equals("Boss")) score += 60;
										scoreLabel.setText("  Score: " + score);
									} else if (alive.get(i).type.equals("Enemy,T1")) {
										alive.get(i).setBackground(Color.GRAY);//有2血量的敵人
									}
								}
							}
						}
					}
					
					for(int i = 0; i < atbr.size(); ++i) {
						alive.remove(atbr.get(i).intValue());
					}
					for(int i = 0; i < tbr.size(); ++i) {
						bul.remove(tbr.get(i).intValue());
					}
				}
			}
		},enemyb, enemyb);
		
		bt = new Timer(); 
		bt.schedule(new TimerTask() { 
			@Override 
			public void run() {
				
				if((t2num == t2lim/2 && buffnum==3) || 
						(t2num == 0 && t1num == t1lim/2 && buffnum == 2) || 
						(t1num == 0 && t2num == 0 && buffnum == 1)) {
					alive.add(buffs[bufflim-buffnum]);
					--buffnum;
				}
				//buffstart == 0 表示現在沒有收到增益效果的加成
				if (buffstart!=0) {//增益效果持續時間為7秒，時間一到，效果消失
					if(System.currentTimeMillis() - buffstart >= 7000) {
						curss = origss;
						buffstart = 0;
					}
				}
				
				//所有敵人都出完的時候，蟹老闆就會出現
				if(t1num == 0 && t2num == 0 && buffnum == 0 && bossnum!=0) {
					for(int i = 0; i < bosslim;++i) {
						alive.add(boss[i]);
						--bossnum;
					}
				}
			}
		},100, 100);
		
		
		bossbullet = new Timer();
		bossbullet.schedule(new TimerTask() {

			@Override
			public void run() {
				if(running) {
					//皮老闆向下發射子弹，每次發射5發
					for(int i = 0; i<5; ++i) {
						for(int b = 0; b<bosslim-bossnum; ++b) {
							if(boss[b].y>=100) enemybul.add(new bullet(boss[b].x + 50, boss[b].y + 50, i-2, 1));
						}
					}
				}
			}
			
			
		}, 2000, 2000);
		
		
		checkv = new Timer();
		checkv.schedule(new TimerTask() {

			@Override
			public void run() {
				if(running) {//如果勝利了，就顯示You win
					//所有敵人都出完了，蟹老闆也被消滅了，就勝利了
					if(alive.isEmpty() && t1num == 0 && t2num == 0&& bossnum == 0) {
						running = false;
						r.setText("   You win!");
						r.setVisible(true);
					}
				}
			}
			
			
		}, 100, 100);
		
		
	}
	
	
	public void show()
	{
		// game.add(bees);
		base.add(options);
		base.add(game);
		frm.add(base);
		frm.setVisible(true);
	}

	public static void main(String[] args) {
		Galaxian a = new Galaxian();
		a.show();
	}
	
	
	
	
	@SuppressWarnings("serial")
	private class FlyingObj extends JPanel //表示敵方和我方的角色
	{
		private String type;
		private int hpLimit = 0;//血量上限
		private int hp = 0;//現在剩餘血量
		public boolean left = false, right = false, up = false, down = false;//是否向左/右/上/下移動
		public JLabel img;

		private double x;//原始坐標
		private double y;
		
		private double xt;//移動方向
		private double yt;
		
		private int moveSpeed = 0;
		public FlyingObj(String t, int hplim) {
			type = t;
			hp = hpLimit = hplim;
			setBackground(Color.WHITE);// default color
			img = new JLabel();
			if (t.equals("Boss")) { 
				xt = 1;
				yt = 1;
				drawBoss();
			} else if (t.equals("Enemy,T1")) { 
				drawEnemyT1();
				xt = 0;
				yt = 1;
			} else if (t.equals("Enemy,T2")) {
				drawEnemyT2();
				xt = 0;
				yt = 1;
			} else if (t.equals("Buff")) {
				drawBuff();
				moveSpeed = 1;
				xt = (int)(Math.random()*2)*6-3;
				yt = 1;
			} else if (t.equals("Self")) {
				drawSelf();
				moveSpeed = 7;
			}

		}
		public void setX(int n){
			this.x = n;
		}

		public void setY(int n){
			this.y = n;
		}
		
		public void setdirection(double xt, double yt)
		{
			this.xt = xt;
			this.yt = yt;
		}
		
		public void move() {
			if (type.equals("Self")) {
				//如果按下了對應方向的按鈕，且沒有出界，就做出對應的移動
				ArrayList<Integer> etbd = new ArrayList<Integer>();
				if (left && x >= 0) this.setX(this.getX() - moveSpeed);
				if (right && x+50 <= 785) this.setX(this.getX() + moveSpeed);
				if (up && y >= 0) this.setY(this.getY() - moveSpeed);
				if (down && y+50 <= 890) this.setY(this.getY() + moveSpeed);
				for(int i = 0; i < alive.size(); ++i) {
					if(alive.get(i).hp > 0 && hit(alive.get(i))) {//如果撞到了東西
						//如果不是增益效果，就生命減一，如果是地方的敵人，則敵人也會損失生命值
						if(!alive.get(i).type.equals("Buff") && System.currentTimeMillis() - lastdeath >= 1500) {
							hero.setLocation(380, 820);
							lastdeath = System.currentTimeMillis();
							--lifes;
							lifeLabel.setText("   Life: " + lifes + " ");
							score -= 25;//死亡扣25分
							scoreLabel.setText("  Score: " + score);
							--alive.get(i).hp;
							
							if (alive.get(i).hp == 0) {
								alive.get(i).setVisible(false);
								etbd.add(i);
							} else if (alive.get(i).type.equals("Enemy,T1")) {
								alive.get(i).setBackground(Color.GRAY);
							}
						} else {//如果是增益效果，獲得攻速加快
							etbd.add(i);
							curss /= 1.75;
							alive.get(i).setVisible(false);
							buffstart = System.currentTimeMillis();
						}
					}
					
					
				}
				
				//如果撞到敵人子彈就會死亡
				ArrayList<Integer> tbd = new ArrayList<Integer>();
				for(int i = 0; i < enemybul.size(); ++i) {
					double x = enemybul.get(i).x;
					double y = enemybul.get(i).y;
					
					if(x+5>hero.x && x+5<hero.x+50 && y+5>hero.y && y+5<hero.y+50 && 
							System.currentTimeMillis() - lastdeath >= 1500) {
						hero.setLocation(380, 820);
						lastdeath = System.currentTimeMillis();
						--lifes;
						lifeLabel.setText("   Life: " + lifes + " ");
						score -= 25;
						scoreLabel.setText("  Score: " + score);
						tbd.add(i);
					}
				}
				for (int i = 0; i<etbd.size(); ++i) {
					alive.remove(etbd.get(i).intValue());
				}
				for (int i = 0; i<tbd.size(); ++i) {
					enemybul.remove(tbd.get(i).intValue());
				}
				
				if(lifes == 0) {
					running = false;
					r.setText("   You loose!");
					r.setVisible(true);
				}
			}
			this.setLocation((int)this.x, (int)this.y);
			
		}

		@SuppressWarnings("deprecation")
		@Override
		public void setBounds(int x, int y, int width, int height) {
			reshape(x, y, width, height);
			this.x = x;
			this.y = y;
		}

		private void drawBoss() {
			setPreferredSize(new Dimension(100, 100));
			setBackground(Color.BLACK);
			ImageIcon ii = new ImageIcon("boss.jpg");
			ImageIcon newi = new ImageIcon(ii.getImage().getScaledInstance(100, 100,  java.awt.Image.SCALE_SMOOTH));
			img.setIcon(newi);
			
			add(img);
		}

		private void drawEnemyT1() {
			setPreferredSize(new Dimension(30, 30));
			setBackground(Color.BLACK);
			ImageIcon ii = new ImageIcon("t1.jpg");
			ImageIcon newi = new ImageIcon(ii.getImage().getScaledInstance(30, 30,  java.awt.Image.SCALE_SMOOTH));
			img.setIcon(newi);
			
			add(img);
		}

		private void drawEnemyT2() {
			setPreferredSize(new Dimension(30, 30));
			setBackground(Color.BLACK);
			ImageIcon ii = new ImageIcon("t2.jpg");
			ImageIcon newi = new ImageIcon(ii.getImage().getScaledInstance(30, 30,  java.awt.Image.SCALE_SMOOTH));
			img.setIcon(newi);
			
			add(img);
		}
		
		private void drawBuff() {
			setPreferredSize(new Dimension(30, 30));
			setBackground(Color.BLACK);
			ImageIcon ii = new ImageIcon("buff.jpg");
			ImageIcon newi = new ImageIcon(ii.getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
			img.setIcon(newi);
			
			add(img);
		}

		private void drawSelf() {
			setPreferredSize(new Dimension(50, 50));
			setBackground(Color.BLACK);
			ImageIcon ii = new ImageIcon("hero.jpg");
			ImageIcon newi = new ImageIcon(ii.getImage().getScaledInstance(50, 50,  java.awt.Image.SCALE_SMOOTH));
			img.setIcon(newi);
			
			add(img);
		}
		
		
		private boolean hit(FlyingObj obj)//如果中心點的距離小於一定值，就會判定為“撞到了”
		{
			//System.out.println(this.getWidth()/2);
			int lx = getX() + this.getWidth()/2;
			int ly = getY() + this.getWidth()/2;
			int rx = obj.getX() + obj.getWidth()/2;
			int ry = obj.getY() + obj.getWidth()/2;
			return Math.pow(((rx-lx)*(rx-lx)+(ry-ly)*(ry-ly)), 0.5) < (this.getWidth()/2+obj.getWidth()/2)-5;
			
		}
	}
}

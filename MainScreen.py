import pygame
from pygame.locals import *
import random
import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

class MainScreen(Screen_abc):

    condition = 1
    dice_num = 0
    #dice = 'img\dice\d1.png'

    def display_dice(self):
        self.dice_num += 1
        if self.dice_num > 4:
            self.dice_num = 0
        #dice_list = ['img\dice\d1.png','img\dice\d2.png','img\dice\d3.png','img\dice\d4.png','img\dice\d5.png','img\dice\d6.png']
        dice_list = ['img\dice\m1.png','img\dice\m2.png','img\dice\m3.png','img\dice\m4.png','img\dice\m5.png']
        return dice_list[self.dice_num]


    def get_event_dice(self):
       # dice_list = ['img\dice\d1.png','img\dice\d2.png','img\dice\d3.png','img\dice\d4.png','img\dice\d5.png','img\dice\d6.png']
        self.dice_num = random.randint(1,6)
    


    # 画面生成
    def display(self):
        super().update()

        super().setBackground(SC.backImg,(0,128,32,32))

    # 背景
        SC.screen.blit(pygame.image.load('img/map/Backgroundimg.png'), self.grid[0][0])
    #島のレイアウト
        SC.screen.blit(pygame.image.load('img\map\hana1.png'), self.grid[28][9])
        SC.screen.blit(pygame.image.load('img\map\hana1.png'), self.grid[21][6])
        SC.screen.blit(pygame.image.load('img\map\kusa.png'), self.grid[24][7])
        SC.screen.blit(pygame.image.load('img\map\kusa.png'), self.grid[26][10])
        SC.screen.blit(pygame.image.load('img\map\mushroom.png'), self.grid[14][12])
        SC.screen.blit(pygame.image.load('img\map\kusa.png'), self.grid[27][6])
        SC.screen.blit(pygame.image.load('img\map\kusa.png'), self.grid[22][9])
        SC.screen.blit(pygame.image.load('img\map\kusa.png'), self.grid[9][6])
        SC.screen.blit(pygame.image.load('img\map\kusa.png'), self.grid[10][8])
        SC.screen.blit(pygame.image.load('img\map\hana1.png'), self.grid[12][6])
        SC.screen.blit(pygame.image.load('img\map\hana2.png'), self.grid[20][12])
        SC.screen.blit(pygame.image.load('img\map\hana2.png'), self.grid[18][12])
        SC.screen.blit(pygame.image.load('img\map\hana2.png'), self.grid[19][11]) 
        SC.screen.blit(pygame.image.load('img\map\eda.png'), self.grid[10][12])  
        SC.screen.blit(pygame.image.load('img\map\kibig.png'), self.grid[17][6])
        SC.screen.blit(pygame.image.load('img\map\Mapsyoki.png'), self.grid[25][7])
        SC.screen.blit(pygame.image.load('img\map\Mapsyoki.png'), self.grid[23][9])
        SC.screen.blit(pygame.image.load('img\map\Mapki.png'), self.grid[12][6])
        SC.screen.blit(pygame.image.load('img\map\Mapki.png'), self.grid[10][8])
        SC.screen.blit(pygame.image.load('img\map\Mapki.png'), self.grid[14][8]) 
        SC.screen.blit(pygame.image.load('img\map\dog1.png'), self.grid[28][9])
        SC.screen.blit(pygame.image.load('img\map\dog2.png'), self.grid[10][6])
        SC.screen.blit(pygame.image.load('img\map\dog3.png'), self.grid[20][11])

        #物件
        SC.screen.blit(pygame.image.load('img\map\船サンプル自作.png'), self.grid[28][4])
        SC.screen.blit(pygame.image.load('img\map\船サンプル自作.png'), self.grid[31][5])
        SC.screen.blit(pygame.image.load('img\map\船サンプル自作.png'), self.grid[31][13])
        SC.screen.blit(pygame.image.load('img\map\船サンプル自作.png'), self.grid[28][14])
        SC.screen.blit(pygame.image.load('img\map\Bukken2.png'), self.grid[29][7])
        SC.screen.blit(pygame.image.load('img\map\Bukken2.png'), self.grid[29][11])

        # プレイヤー情報欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        for i in range(4):
            super().setBox(SC.Black, (i*32*10, 0), 32*10, 32*3, 3) # 外枠
            display_player_color = pygame.Rect(i*32*10+3, 3, 32*10-3, 32*3-3)  # 背景色
            pygame.draw.rect(SC.screen, SC.White, display_player_color) # 背景色を枠内に配置
            SC.screen.blit(pygame.image.load('img/Ozaki.png'), ((32*2+16)+(i*32*10), 32+18)) # プレイヤーアイコン
            SC.screen.blit(pygame.image.load('img/Coin.png'), ((32*6+8)+(i*32*10), 32-12)) # コインアイコン
            SC.screen.blit(pygame.image.load('img/Building1.png'), ((32*6+8)+(i*32*10), 32+18)) # 物件アイコン
            super().setText_S('Player'+str(i+1), ((32*2)+(i*32*10), 32-14), 22, SC.Black) # プレイヤー名（仮）
            super().setText_L(str(i+1), ((32*1+2)+(i*32*10), 32+22), 26, SC.Black) # 順位（仮）
            super().setText_S('0枚', ((32*7+16)+(i*32*10), 32-16), 22, SC.Black) # コイン数
            super().setText_S('0件', ((32*7+16)+(i*32*10), 32+18), 22, SC.Black) # 物件数
            i += 1
        pygame.draw.rect(SC.screen, SC.Black, pygame.Rect(32*40-3, 32*0, 3, 32*3)) # 右端の外枠線を追加

        # プレイヤー情報欄の現在のプレイヤーのカーソル（仮）
        super().setText_S('●', (32*1, 32-12), 20, SC.Red)

        # 青マスを上辺と下辺に配置
        for i in range(12):
            SC.screen.blit(pygame.image.load('img/Blue.png'), self.grid[8+i*2][5])
            SC.screen.blit(pygame.image.load('img/Blue.png'), self.grid[8+i*2][13])
            i += 1

        # 青マスを左辺と右辺に配置
        for i in range(3):
            SC.screen.blit(pygame.image.load('img/Blue.png'), self.grid[8][7+i*2])
            SC.screen.blit(pygame.image.load('img/Blue.png'), self.grid[30][7+i*2])
            i += 1

        # 赤マスを上辺と下辺に配置
        for i in range(3):
            SC.screen.blit(pygame.image.load('img/Red.png'), self.grid[12+i*8][5])
            SC.screen.blit(pygame.image.load('img/Red.png'), self.grid[10+i*8][13])
            i += 1

        # 赤マスを左辺に配置
        SC.screen.blit(pygame.image.load('img/Red.png'), self.grid[8][9])

        # 黄色マス（物件マス）を配置
        SC.screen.blit(pygame.image.load('img/Yellow.png'), self.grid[24][5])
        SC.screen.blit(pygame.image.load('img/Yellow.png'), self.grid[22][13])

        # オレンジ色マス（ボーナスマス）を配置
        SC.screen.blit(pygame.image.load('img/Orange.png'), self.grid[14][13])

        # 紫色マス（特大マイナスマス）を配置
        SC.screen.blit(pygame.image.load('img/Purple.png'), self.grid[30][9])

        #イベントマス（オブジェクト）
        SC.screen.blit(pygame.image.load('img\map\Bukken1.png'), self.grid[26][13])
        SC.screen.blit(pygame.image.load('img\map\Bukken1.png'), self.grid[8][11])
        SC.screen.blit(pygame.image.load('img\map\Bukken1.png'), self.grid[20][5])

        # 物件を配置（仮）
        # SC.screen.blit(pygame.image.load('img/Building2.png'), (32*24, 32*3+18))
        # SC.screen.blit(pygame.image.load('img/Building2.png'), (32*22, 32*11+13))

        # アイテムを配置（仮）
        # SC.screen.blit(pygame.image.load('img/Item.png'), (32*29, 32*11+5))
        # SC.screen.blit(pygame.image.load('img/Item.png'), (32*20+5, 32*12))

        # マス上に各プレイヤーを配置（仮）
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), self.grid[14][5]) # 現在のプレイヤー
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), self.grid[26][5])
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), self.grid[30][5])
        SC.screen.blit(pygame.image.load('img/Ozaki.png'), self.grid[24][13])

        # マス上の現在のプレイヤーのカーソル（仮）
        super().setText_S('▼', self.grid[14][4], 32, SC.Red) # 現在のプレイヤー
        super().setText_S('▼', self.grid[24][12], 32, SC.Blue)

        # ターン表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        display_turn_color = pygame.Rect(32*1, 32*5, 32*5, 32*9)
        pygame.draw.rect(SC.screen, SC.White, display_turn_color)
        super().setTextBox_S('', SC.Black, SC.Black, self.grid[1][5], 32*5, 32*9, 3, 25, 10, 10)
        super().setText_S('ターン', (32*2, 32*6), 35, SC.Black)
        super().setText_S('3/15', (32*2+5, 32*8+10), 45, SC.Black)
        super().setText_S('【序盤】', (32+12, 32*11+10), 35, SC.Black)

        # ゲーム終了ボタン
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        button_color = pygame.Rect(32*1, 32*16, 32*5, 32*2)
        pygame.draw.rect(SC.screen, SC.White, button_color)
        super().setTextBox_S('', SC.Black, SC.Black, self.grid[1][16], 32*5, 32*2, 3, 25, 10, 10)
        super().setText_S('ゲーム終了', (32*1+16, 32*16+20), 25, SC.Black)

        # 説明表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        display_desc_color = pygame.Rect(32*8, 32*15, 32*23, 32*4)
        pygame.draw.rect(SC.screen, SC.White, display_desc_color)
        text = ['アイテム名：BBBBB', '　アイテムの説明']
        super().setTextBox_S(text, SC.Black, SC.Black, self.grid[8][15], 32*23, 32*4, 3, 30, 20, 20)

        # アイテム表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        super().setText_L('アイテム', (32*35, 32*10), 24, SC.Black)
        display_item_color = pygame.Rect(32*34, 32*11, 32*5, 32*3)
        pygame.draw.rect(SC.screen, SC.White, display_item_color)
        text = ['▼AAAAA', '▼BBBBB', '▼CCCCC']
        super().setTextBox_S(text, SC.Black, SC.Black, self.grid[34][11], 32*5, 32*3, 3, 25, 10, 10)
        super().setText_S('←', (32*37+12, 32*12+2), 30, SC.Red)

        # サイコロ表示欄
        #SC.screen.blit(pygame.image.load('img/Dice1.jpg'), self.grid[35][5])
        if self.condition == 1:
           SC.screen.blit(pygame.image.load(self.display_dice()), self.grid[35][5])
        if self.condition == 2:
            SC.screen.blit(pygame.image.load('img\dice\d' + str(self.dice_num) + '.png'), self.grid[35][5])

    # イベント処理
    def getEvent(self):
        for event in pygame.event.get():
            # 終了用のイベント処理
            if event.type == QUIT:  # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                if event.key == K_ESCAPE:  # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()
                # if event.key == K_SPACE:
                #     SC.ScreenNum = 1 
                if event.key == K_SPACE: #「スペース」キーを押したとき
                    if self.condition == 1:
                        self.get_event_dice()
                        self.condition = 2 #サイコロが止まる。
                if event.key == K_DOWN: #「↓」が押されたとき
                    self.condition = 1

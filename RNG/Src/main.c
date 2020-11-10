/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2020 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
uint32_t MyRandomNumber[7];
uint32_t sendValue[7];
uint8_t flagRNG = 0;

uint8_t Rx_data[10];
uint8_t Tx_data[50];
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
RNG_HandleTypeDef hrng;

UART_HandleTypeDef huart3;

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_RNG_Init(void);
static void MX_USART3_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
void HAL_RNG_ReadyDataCallback(RNG_HandleTypeDef *hrng, uint32_t random32bit)
{
  /* Prevent unused argument(s) compilation warning */
  UNUSED(hrng);
  UNUSED(random32bit);
  /* NOTE : This function should not be modified. When the callback is needed,
            function HAL_RNG_ReadyDataCallback must be implemented in the user file.
   */
	flagRNG = 1;
}

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_RNG_Init();
  MX_USART3_UART_Init();
  /* USER CODE BEGIN 2 */
	HAL_RNG_GenerateRandomNumber_IT(&hrng);
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {	
		if(flagRNG)
		{
			flagRNG = 1;
			for(int i=0;i<=6;i++)
				{
					MyRandomNumber[i] = HAL_RNG_ReadLastRandomNumber(&hrng);
					MyRandomNumber[i] = MyRandomNumber[i]%100;
					HAL_RNG_GenerateRandomNumber_IT(&hrng);
				}
		}
		
		/*
			MyRandomNumber[0] => AC - Current  - For Efficiency
		  MyRandomNumber[1] => AC - Voltage  - For Efficiency
		  MyRandomNumber[2] => DC - Current  - For Efficiency
		  MyRandomNumber[3] => DC - Voltage  - For Efficiency
		  MyRandomNumber[4] => NTC					 - For Efficiency
		
		  MyRandomNumber[5] => DC - Current  - For Electric Load
		  MyRandomNumber[6] => DC - Voltage  - For Electric Load
		
		*/

		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",100),1);
		HAL_Delay(1);		
		
		for(int a=0;a<=6;a++)
			{	
				if(a == 0)
					{
						MyRandomNumber[a] = MyRandomNumber[a] % 10;
		        HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[a]),1);
					  HAL_Delay(1);						
					}
				else if(a == 1)
					{
						MyRandomNumber[a] = MyRandomNumber[a] % 50;
						HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[a]),1);
						HAL_Delay(1);
					}
				else if(a == 2)
					{
						MyRandomNumber[a] = MyRandomNumber[a] % 10;
						HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[a]),1);
						HAL_Delay(1);
					}	
				else if(a == 3)
					{
						MyRandomNumber[a] = MyRandomNumber[a] % 50;
						HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[a]),1);
						HAL_Delay(1);
					}			
				else if(a == 4)
					{
						MyRandomNumber[a] = MyRandomNumber[a] % 50;
						HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[a]),1);
						HAL_Delay(1);
					}	
				else if(a == 5)
					{
						MyRandomNumber[a] = MyRandomNumber[a] % 10;
						HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[a]),1);
						HAL_Delay(1);
					}	
				else
					{
						MyRandomNumber[a] = MyRandomNumber[a] % 50;
						HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[a]),1);
						HAL_Delay(1);
					}
			}

//		// AC-C
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"a\n"),1);
//		HAL_Delay(10);						
//		MyRandomNumber[0] = MyRandomNumber[0] % 10;
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[0]),1);
//		HAL_Delay(10);	
//		
//		// AC-V
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"b\n"),1);
//		HAL_Delay(10);	
//		MyRandomNumber[1] = MyRandomNumber[1] % 50;
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[1]),1);
//		HAL_Delay(10);	
//		
//		// DC-C1
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"c\n"),1);
//		HAL_Delay(10);	
//		MyRandomNumber[2] = MyRandomNumber[2] % 10;
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[2]),1);
//		HAL_Delay(10);	
//		
//		// DC-V1
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"d\n"),1);
//		HAL_Delay(10);	
//		MyRandomNumber[3] = MyRandomNumber[3] % 50;
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[3]),1);
//		HAL_Delay(10);	
//		
//		// NTC
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"e\n"),1);
//		HAL_Delay(10);	
//		MyRandomNumber[4] = MyRandomNumber[4] % 50;
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[4]),1);
//		HAL_Delay(10);	
//		
//		// DC-C2
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"f\n"),1);
//		HAL_Delay(10);	
//		MyRandomNumber[5] = MyRandomNumber[5] % 10;
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[5]),1);
//		HAL_Delay(10);	
//		
//		// DC-V2
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"a\n"),1);
//		HAL_Delay(10);	
//		MyRandomNumber[6] = MyRandomNumber[6] % 50;
//		HAL_UART_Transmit(&huart3,Tx_data,sprintf(Tx_data,"%d\n",MyRandomNumber[6]),1);
//		HAL_Delay(10);	
					
			
		
		HAL_UART_Receive(&huart3,Rx_data,10,1);	
	
	  if(Rx_data[0] == '1')
		HAL_GPIO_WritePin(GPIOD, GPIO_PIN_12|GPIO_PIN_13|GPIO_PIN_14|GPIO_PIN_15, GPIO_PIN_SET);
		if(Rx_data[0] == '0')
		HAL_GPIO_WritePin(GPIOD, GPIO_PIN_12|GPIO_PIN_13|GPIO_PIN_14|GPIO_PIN_15, GPIO_PIN_RESET);
    /* USER CODE END WHILE */
		
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);
  /** Initializes the CPU, AHB and APB busses clocks
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSI;
  RCC_OscInitStruct.PLL.PLLM = 8;
  RCC_OscInitStruct.PLL.PLLN = 168;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 8;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB busses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV2;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_5) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief RNG Initialization Function
  * @param None
  * @retval None
  */
static void MX_RNG_Init(void)
{

  /* USER CODE BEGIN RNG_Init 0 */

  /* USER CODE END RNG_Init 0 */

  /* USER CODE BEGIN RNG_Init 1 */

  /* USER CODE END RNG_Init 1 */
  hrng.Instance = RNG;
  if (HAL_RNG_Init(&hrng) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN RNG_Init 2 */

  /* USER CODE END RNG_Init 2 */

}

/**
  * @brief USART3 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART3_UART_Init(void)
{

  /* USER CODE BEGIN USART3_Init 0 */

  /* USER CODE END USART3_Init 0 */

  /* USER CODE BEGIN USART3_Init 1 */

  /* USER CODE END USART3_Init 1 */
  huart3.Instance = USART3;
  huart3.Init.BaudRate = 115200;
  huart3.Init.WordLength = UART_WORDLENGTH_8B;
  huart3.Init.StopBits = UART_STOPBITS_1;
  huart3.Init.Parity = UART_PARITY_NONE;
  huart3.Init.Mode = UART_MODE_TX_RX;
  huart3.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart3.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart3) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART3_Init 2 */

  /* USER CODE END USART3_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();
  __HAL_RCC_GPIOD_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOD, GPIO_PIN_12|GPIO_PIN_13|GPIO_PIN_14|GPIO_PIN_15, GPIO_PIN_RESET);

  /*Configure GPIO pin : PA0 */
  GPIO_InitStruct.Pin = GPIO_PIN_0;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pins : PD12 PD13 PD14 PD15 */
  GPIO_InitStruct.Pin = GPIO_PIN_12|GPIO_PIN_13|GPIO_PIN_14|GPIO_PIN_15;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOD, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */

  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     tex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/

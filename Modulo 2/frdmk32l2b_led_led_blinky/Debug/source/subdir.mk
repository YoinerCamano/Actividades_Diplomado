################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../source/led_blinky.c \
../source/mtb.c \
../source/semihost_hardfault.c 

C_DEPS += \
./source/led_blinky.d \
./source/mtb.d \
./source/semihost_hardfault.d 

OBJS += \
./source/led_blinky.o \
./source/mtb.o \
./source/semihost_hardfault.o 


# Each subdirectory must supply rules for building sources it contributes
source/%.o: ../source/%.c source/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -std=gnu99 -D__REDLIB__ -DCPU_K32L2B31VLH0A -DCPU_K32L2B31VLH0A_cm0plus -DFRDM_K32L2B -DFREEDOM -DMCUXPRESSO_SDK -DSDK_DEBUGCONSOLE=1 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=0 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"C:\Users\yoine\OneDrive - Universidad del Magdalena\Diplomado IoT\Actividades\Modulo 2\frdmk32l2b_led_led_blinky\source" -I"C:\Users\yoine\OneDrive - Universidad del Magdalena\Diplomado IoT\Actividades\Modulo 2\frdmk32l2b_led_led_blinky\utilities" -I"C:\Users\yoine\OneDrive - Universidad del Magdalena\Diplomado IoT\Actividades\Modulo 2\frdmk32l2b_led_led_blinky\drivers" -I"C:\Users\yoine\OneDrive - Universidad del Magdalena\Diplomado IoT\Actividades\Modulo 2\frdmk32l2b_led_led_blinky\device" -I"C:\Users\yoine\OneDrive - Universidad del Magdalena\Diplomado IoT\Actividades\Modulo 2\frdmk32l2b_led_led_blinky\component\uart" -I"C:\Users\yoine\OneDrive - Universidad del Magdalena\Diplomado IoT\Actividades\Modulo 2\frdmk32l2b_led_led_blinky\component\lists" -I"C:\Users\yoine\OneDrive - Universidad del Magdalena\Diplomado IoT\Actividades\Modulo 2\frdmk32l2b_led_led_blinky\CMSIS" -I"C:\Users\yoine\OneDrive - Universidad del Magdalena\Diplomado IoT\Actividades\Modulo 2\frdmk32l2b_led_led_blinky\board" -O0 -fno-common -g3 -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m0plus -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-source

clean-source:
	-$(RM) ./source/led_blinky.d ./source/led_blinky.o ./source/mtb.d ./source/mtb.o ./source/semihost_hardfault.d ./source/semihost_hardfault.o

.PHONY: clean-source


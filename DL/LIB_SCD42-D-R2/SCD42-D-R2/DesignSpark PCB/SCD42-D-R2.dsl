SamacSys ECAD Model
15531867/976295/2.49/21/3/Integrated Circuit

DESIGNSPARK_INTERMEDIATE_ASCII

(asciiHeader
	(fileUnits MM)
)
(library Library_1
	(padStyleDef "r150_80"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 0.800) (shapeHeight 1.500))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0) (shapeHeight 0))
	)
	(padStyleDef "s480"
		(holeDiam 0)
		(padShape (layerNumRef 1) (padShapeType Rect)  (shapeWidth 4.800) (shapeHeight 4.800))
		(padShape (layerNumRef 16) (padShapeType Ellipse)  (shapeWidth 0) (shapeHeight 0))
	)
	(textStyleDef "Default"
		(font
			(fontType Stroke)
			(fontFace "Helvetica")
			(fontHeight 50 mils)
			(strokeWidth 5 mils)
		)
	)
	(patternDef "SCD42DR2" (originalName "SCD42DR2")
		(multiLayer
			(pad (padNum 1) (padStyleRef r150_80) (pt -4.000, 2.500) (rotation 90))
			(pad (padNum 2) (padStyleRef r150_80) (pt -4.000, 1.250) (rotation 90))
			(pad (padNum 3) (padStyleRef r150_80) (pt -4.000, 0.000) (rotation 90))
			(pad (padNum 4) (padStyleRef r150_80) (pt -4.000, -1.250) (rotation 90))
			(pad (padNum 5) (padStyleRef r150_80) (pt -4.000, -2.500) (rotation 90))
			(pad (padNum 6) (padStyleRef r150_80) (pt -2.500, -4.000) (rotation 0))
			(pad (padNum 7) (padStyleRef r150_80) (pt -1.250, -4.000) (rotation 0))
			(pad (padNum 8) (padStyleRef r150_80) (pt 0.000, -4.000) (rotation 0))
			(pad (padNum 9) (padStyleRef r150_80) (pt 1.250, -4.000) (rotation 0))
			(pad (padNum 10) (padStyleRef r150_80) (pt 2.500, -4.000) (rotation 0))
			(pad (padNum 11) (padStyleRef r150_80) (pt 4.000, -2.500) (rotation 90))
			(pad (padNum 12) (padStyleRef r150_80) (pt 4.000, -1.250) (rotation 90))
			(pad (padNum 13) (padStyleRef r150_80) (pt 4.000, 0.000) (rotation 90))
			(pad (padNum 14) (padStyleRef r150_80) (pt 4.000, 1.250) (rotation 90))
			(pad (padNum 15) (padStyleRef r150_80) (pt 4.000, 2.500) (rotation 90))
			(pad (padNum 16) (padStyleRef r150_80) (pt 2.500, 4.000) (rotation 0))
			(pad (padNum 17) (padStyleRef r150_80) (pt 1.250, 4.000) (rotation 0))
			(pad (padNum 18) (padStyleRef r150_80) (pt 0.000, 4.000) (rotation 0))
			(pad (padNum 19) (padStyleRef r150_80) (pt -1.250, 4.000) (rotation 0))
			(pad (padNum 20) (padStyleRef r150_80) (pt -2.500, 4.000) (rotation 0))
			(pad (padNum 21) (padStyleRef s480) (pt 0.000, 0.000) (rotation 90))
		)
		(layerContents (layerNumRef 18)
			(attr "RefDes" "RefDes" (pt 0.000, -0.000) (textStyleRef "Default") (isVisible True))
		)
		(layerContents (layerNumRef 28)
			(line (pt -5.05 -5.05) (pt 5.05 -5.05) (width 0.1))
		)
		(layerContents (layerNumRef 28)
			(line (pt 5.05 -5.05) (pt 5.05 5.05) (width 0.1))
		)
		(layerContents (layerNumRef 28)
			(line (pt 5.05 5.05) (pt -5.05 5.05) (width 0.1))
		)
		(layerContents (layerNumRef 28)
			(line (pt -5.05 5.05) (pt -5.05 -5.05) (width 0.1))
		)
		(layerContents (layerNumRef 30)
			(line (pt -6.05 6.05) (pt 6.05 6.05) (width 0.1))
		)
		(layerContents (layerNumRef 30)
			(line (pt 6.05 6.05) (pt 6.05 -6.05) (width 0.1))
		)
		(layerContents (layerNumRef 30)
			(line (pt 6.05 -6.05) (pt -6.05 -6.05) (width 0.1))
		)
		(layerContents (layerNumRef 30)
			(line (pt -6.05 -6.05) (pt -6.05 6.05) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt -3.4 5.05) (pt -5.05 5.05) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -5.05 5.05) (pt -5.05 3.4) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -5.05 -3.4) (pt -5.05 -5.05) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -5.05 -5.05) (pt -3.4 -5.05) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 3.4 -5.05) (pt 5.05 -5.05) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 5.05 -5.05) (pt 5.05 -3.4) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 5.05 3.4) (pt 5.05 5.05) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt 5.05 5.05) (pt 3.4 5.05) (width 0.2))
		)
		(layerContents (layerNumRef 18)
			(line (pt -5.6 2.5) (pt -5.6 2.5) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(arc (pt -5.65, 2.5) (radius 0.05) (startAngle .0) (sweepAngle 180.0) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(line (pt -5.7 2.5) (pt -5.7 2.5) (width 0.1))
		)
		(layerContents (layerNumRef 18)
			(arc (pt -5.65, 2.5) (radius 0.05) (startAngle 180.0) (sweepAngle 180.0) (width 0.1))
		)
	)
	(symbolDef "SCD42-D-R2" (originalName "SCD42-D-R2")

		(pin (pinNum 1) (pt 0 mils 0 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -25 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 2) (pt 0 mils -100 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -125 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 3) (pt 0 mils -200 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -225 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 4) (pt 0 mils -300 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -325 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 5) (pt 0 mils -400 mils) (rotation 0) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 230 mils -425 mils) (rotation 0]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 6) (pt 400 mils -1100 mils) (rotation 90) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 425 mils -870 mils) (rotation 90]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 7) (pt 500 mils -1100 mils) (rotation 90) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 525 mils -870 mils) (rotation 90]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 8) (pt 600 mils -1100 mils) (rotation 90) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 625 mils -870 mils) (rotation 90]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 9) (pt 700 mils -1100 mils) (rotation 90) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 725 mils -870 mils) (rotation 90]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 10) (pt 800 mils -1100 mils) (rotation 90) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 825 mils -870 mils) (rotation 90]) (justify "Left") (textStyleRef "Default"))
		))
		(pin (pinNum 11) (pt 1300 mils -400 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 1070 mils -425 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 12) (pt 1300 mils -300 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 1070 mils -325 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 13) (pt 1300 mils -200 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 1070 mils -225 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 14) (pt 1300 mils -100 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 1070 mils -125 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 15) (pt 1300 mils 0 mils) (rotation 180) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 1070 mils -25 mils) (rotation 0]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 16) (pt 900 mils 700 mils) (rotation 270) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 925 mils 470 mils) (rotation 90]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 17) (pt 800 mils 700 mils) (rotation 270) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 825 mils 470 mils) (rotation 90]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 18) (pt 700 mils 700 mils) (rotation 270) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 725 mils 470 mils) (rotation 90]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 19) (pt 600 mils 700 mils) (rotation 270) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 625 mils 470 mils) (rotation 90]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 20) (pt 500 mils 700 mils) (rotation 270) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 525 mils 470 mils) (rotation 90]) (justify "Right") (textStyleRef "Default"))
		))
		(pin (pinNum 21) (pt 400 mils 700 mils) (rotation 270) (pinLength 200 mils) (pinDisplay (dispPinName true)) (pinName (text (pt 425 mils 470 mils) (rotation 90]) (justify "Right") (textStyleRef "Default"))
		))
		(line (pt 200 mils 500 mils) (pt 1100 mils 500 mils) (width 6 mils))
		(line (pt 1100 mils 500 mils) (pt 1100 mils -900 mils) (width 6 mils))
		(line (pt 1100 mils -900 mils) (pt 200 mils -900 mils) (width 6 mils))
		(line (pt 200 mils -900 mils) (pt 200 mils 500 mils) (width 6 mils))
		(attr "RefDes" "RefDes" (pt 1150 mils 700 mils) (justify Left) (isVisible True) (textStyleRef "Default"))

	)
	(compDef "SCD42-D-R2" (originalName "SCD42-D-R2") (compHeader (numPins 21) (numParts 1) (refDesPrefix IC)
		)
		(compPin "1" (pinName "DNC_1") (partNum 1) (symPinNum 1) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "2" (pinName "DNC_2") (partNum 1) (symPinNum 2) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "3" (pinName "DNC_3") (partNum 1) (symPinNum 3) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "4" (pinName "DNC_4") (partNum 1) (symPinNum 4) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "5" (pinName "DNC_5") (partNum 1) (symPinNum 5) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "6" (pinName "GND_1") (partNum 1) (symPinNum 6) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "7" (pinName "VDD") (partNum 1) (symPinNum 7) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "8" (pinName "DNC_6") (partNum 1) (symPinNum 8) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "9" (pinName "SCL") (partNum 1) (symPinNum 9) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "10" (pinName "SDA") (partNum 1) (symPinNum 10) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "11" (pinName "DNC_7") (partNum 1) (symPinNum 11) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "12" (pinName "DNC_8") (partNum 1) (symPinNum 12) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "13" (pinName "DNC_9") (partNum 1) (symPinNum 13) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "14" (pinName "DNC_10") (partNum 1) (symPinNum 14) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "15" (pinName "DNC_11") (partNum 1) (symPinNum 15) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "16" (pinName "DNC_12") (partNum 1) (symPinNum 16) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "17" (pinName "DNC_13") (partNum 1) (symPinNum 17) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "18" (pinName "DNC_14") (partNum 1) (symPinNum 18) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "19" (pinName "VDDH") (partNum 1) (symPinNum 19) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "20" (pinName "GND_2") (partNum 1) (symPinNum 20) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(compPin "21" (pinName "GND_3") (partNum 1) (symPinNum 21) (gateEq 0) (pinEq 0) (pinType Bidirectional))
		(attachedSymbol (partNum 1) (altType Normal) (symbolName "SCD42-D-R2"))
		(attachedPattern (patternNum 1) (patternName "SCD42DR2")
			(numPads 21)
			(padPinMap
				(padNum 1) (compPinRef "1")
				(padNum 2) (compPinRef "2")
				(padNum 3) (compPinRef "3")
				(padNum 4) (compPinRef "4")
				(padNum 5) (compPinRef "5")
				(padNum 6) (compPinRef "6")
				(padNum 7) (compPinRef "7")
				(padNum 8) (compPinRef "8")
				(padNum 9) (compPinRef "9")
				(padNum 10) (compPinRef "10")
				(padNum 11) (compPinRef "11")
				(padNum 12) (compPinRef "12")
				(padNum 13) (compPinRef "13")
				(padNum 14) (compPinRef "14")
				(padNum 15) (compPinRef "15")
				(padNum 16) (compPinRef "16")
				(padNum 17) (compPinRef "17")
				(padNum 18) (compPinRef "18")
				(padNum 19) (compPinRef "19")
				(padNum 20) (compPinRef "20")
				(padNum 21) (compPinRef "21")
			)
		)
		(attr "Manufacturer_Name" "Sensirion")
		(attr "Manufacturer_Part_Number" "SCD42-D-R2")
		(attr "Mouser Part Number" "403-SCD42-D-R2")
		(attr "Mouser Price/Stock" "https://www.mouser.co.uk/ProductDetail/Sensirion/SCD42-D-R2?qs=A6eO%252BMLsxmSRIzSbnJAIXA%3D%3D")
		(attr "Arrow Part Number" "SCD42-D-R2")
		(attr "Arrow Price/Stock" "https://www.arrow.com/en/products/scd42-d-r2/sensirion-ag?region=nac")
		(attr "Mouser Testing Part Number" "")
		(attr "Mouser Testing Price/Stock" "")
		(attr "Description" "Air Quality Sensors CO2 Sensor for US HVAC applications")
		(attr "Datasheet Link" "https://sensirion.com/media/documents/BD775C74/623DE486/CD_DS_SCD42_Datasheet_D1.pdf")
		(attr "Height" "6.8 mm")
	)

)

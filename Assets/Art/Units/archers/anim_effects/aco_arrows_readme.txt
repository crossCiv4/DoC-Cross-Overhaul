COMPOSITE ARCHER ARROWS MANAGEMENT

If you wish to preserve the right kind of arrow during combat animation sequence, you must:

1) append the following code into your modded CIV4EffectInfos.xml, editing the <Path> rows below:

		<!-- composite archer arrows:-->
		<EffectInfo>
			<Type>EFFECT_CHINESEARROW1</Type>
			<Description>ChineseArcherArrow</Description>
			<fScale>1.0</fScale>
			<fUpdateRate>1.0</fUpdateRate>
			<Path>[...your path...]/anim_effects/aco_arrow1.nif</Path>
			<bIsProjectile>1</bIsProjectile>
			<fSpeed>500.0</fSpeed>
			<fArcValue>0.0</fArcValue>
		</EffectInfo>
		<EffectInfo>
			<Type>EFFECT_CHINESEARROW2</Type>
			<Description>ChineseArcherArrow</Description>
			<fScale>1.0</fScale>
			<fUpdateRate>1.0</fUpdateRate>
			<Path>[...your path...]/anim_effects/aco_arrow2.nif</Path>
			<bIsProjectile>1</bIsProjectile>
			<fSpeed>500.0</fSpeed>
			<fArcValue>0.0</fArcValue>
		</EffectInfo>
		<EffectInfo>
			<Type>EFFECT_CHINESEARROW3</Type>
			<Description>ChineseArcherArrow</Description>
			<fScale>1.0</fScale>
			<fUpdateRate>1.0</fUpdateRate>
			<Path>[...your path...]/anim_effects/aco_arrow3.nif</Path>
			<bIsProjectile>1</bIsProjectile>
			<fSpeed>500.0</fSpeed>
			<fArcValue>0.0</fArcValue>
		</EffectInfo>
		<EffectInfo>
			<Type>EFFECT_CHINESEARROW4</Type>
			<Description>ChineseArcherArrow</Description>
			<fScale>1.0</fScale>
			<fUpdateRate>1.0</fUpdateRate>
			<Path>[...your path...]/anim_effects/aco_arrow4.nif</Path>
			<bIsProjectile>1</bIsProjectile>
			<fSpeed>500.0</fSpeed>
			<fArcValue>0.0</fArcValue>
		</EffectInfo>

2) address the right kind of kfm into <KFM> rows of your modded CIV4ArtDefines_Unit.xml as follow:

for archers using light brown arrows:
			<KFM>[...your path...]/anim_comp/archer_1.kfm</KFM>
 
for archers using dark brown arrows:
			<KFM>[...your path...]/anim_comp/archer_2.kfm</KFM>
 
for archers using babylonian (gold&black) arrows:
			<KFM>[...your path...]/anim_comp/archer_3.kfm</KFM>
 
for archers using minoan (white&black) arrows:
			<KFM>[...your path...]/anim_comp/archer_4.kfm</KFM>
			
During combat sequence, each modded #_kfm calls its rangedstrik#.kf animation, each #.kf calls its EFFECT_XXX xml <Type>, each EFFECT_XXX calls its effect-nif properly.
 
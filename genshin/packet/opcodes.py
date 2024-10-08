import enum


class Opcode(enum.IntEnum):
    ReliquaryUpgradeRsp = 5692
    TakeInvestigationRewardReq = 20220
    DungeonWayPointActivateRsp = 21846
    AvatarUpgradeRsp = 24717
    MarkNewNotify = 5979
    AvatarDelNotify = 8219
    EvtAvatarEnterFocusNotify = 4109
    DungeonChallengeBeginNotify = 28604
    HomeAvatarSummonFinishRsp = 8835
    FleurFairMusicGameSettleReq = 22852
    ToTheMoonQueryPathRsp = 6148
    SceneForceUnlockNotify = 2583
    HomeKickPlayerReq = 24840
    CheckUgcStateRsp = 7329
    SetPlayerBirthdayRsp = 9150
    VehicleInteractRsp = 27433
    CombatInvocationsNotify = 5253
    MuqadasPotionDungeonSettleNotify = 2813
    HomeAvatarCostumeChangeNotify = 7004
    SetUpLunchBoxWidgetReq = 24935
    HomeChangeBgmRsp = 6476
    HomeChangeEditModeRsp = 2916
    TryEnterHomeRsp = 21829
    AvatarDieAnimationEndRsp = 20675
    OpenStateUpdateNotify = 29093
    HomeChooseModuleRsp = 2292
    FireworksReformDataNotify = 23329
    ReliquaryDecomposeRsp = 8148
    GetUgcRsp = 29873
    PullRecentChatReq = 6977
    MonsterForceAlertNotify = 5287
    HomeUpdateArrangementInfoRsp = 25852
    NpcTalkReq = 24255
    MassiveEntityElementOpBatchNotify = 25032
    DungeonDieOptionReq = 4398
    ChangeMpTeamAvatarReq = 26305
    ForgeQueueManipulateReq = 23681
    SceneForceLockNotify = 27356
    HomeNewUnlockedBgmIdListNotify = 9140
    TakeBattlePassRewardReq = 27855
    FurnitureMakeRsp = 7783
    ReformFireworksRsp = 8112
    GetAllMailNotify = 7646
    StartCoopPointRsp = 1231
    HomeSceneInitFinishRsp = 9038
    AvatarChangeElementTypeReq = 4974
    GetMailItemRsp = 9691
    WearEquipReq = 7023
    PlayerStoreNotify = 7845
    AskAddFriendReq = 23646
    HomeAvatarSummonEventRsp = 27614
    PlayerApplyEnterHomeResultRsp = 5358
    WidgetDoBagRsp = 9170
    GetCompoundDataRsp = 28257
    ClientAbilityInitFinishNotify = 28413
    BattlePassAllDataNotify = 27624
    WidgetSlotChangeNotify = 24715
    BackMyWorldRsp = 23771
    PlayerGameTimeNotify = 4423
    SceneEntityAppearNotify = 6263
    GetPlayerSocialDetailReq = 3597
    LifeStateChangeNotify = 29321
    HomeGetArrangementInfoRsp = 9688
    BuyGoodsReq = 23649
    StoreItemChangeNotify = 2646
    PlayerSetPauseReq = 8076
    BatchBuyGoodsReq = 21323
    WeaponAwakenRsp = 1182
    GetPlayerHomeCompInfoReq = 23660
    ForgeGetQueueDataReq = 5954
    PlayerChatRsp = 29270
    UpdatePlayerShowNameCardListReq = 7487
    HomeResourceTakeHomeCoinReq = 4728
    SetFriendEnterHomeOptionReq = 20740
    CookDataNotify = 25816
    GetInvestigationMonsterReq = 21813
    ExitTransPointRegionNotify = 8012
    AvatarExpeditionDataNotify = 22907
    DealAddFriendReq = 21886
    HomeChangeBgmNotify = 29481
    AvatarChangeCostumeNotify = 5367
    FireworksLaunchDataNotify = 2905
    HomeComfortInfoNotify = 279
    ServerGlobalValueChangeNotify = 25816
    GetAllActivatedBargainDataRsp = 3517
    MusicGameStartReq = 2690
    WidgetGadgetDataNotify = 380
    BargainOfferPriceRsp = 28942
    GetAllMailResultNotify = 20649
    FurnitureMakeStartRsp = 21400
    HomeSceneJumpRsp = 28622
    GetBargainDataReq = 7358
    ChooseCurAvatarTeamReq = 27622
    PingRsp = 22595
    CodexDataUpdateNotify = 27330
    HomeEnterEditModeFinishRsp = 28448
    UseItemReq = 9576
    GetScenePointRsp = 29349
    SetPlayerNameRsp = 24044
    DungeonShowReminderNotify = 7524
    EnterSceneDoneRsp = 793
    MonsterAIConfigHashNotify = 1317
    ScenePointUnlockNotify = 21959
    SetPlayerPropRsp = 20930
    WidgetCoolDownNotify = 29375
    CloseCommonTipsNotify = 27695
    GachaWishRsp = 26208
    DoGachaRsp = 20937
    DailyTaskFilterCityRsp = 8986
    PlayerEnterDungeonRsp = 3067
    AvatarExpeditionCallBackReq = 22881
    GetProfilePictureDataReq = 22511
    GetFriendShowAvatarInfoReq = 20766
    PlayerLoginReq = 2422
    ChangeTeamNameReq = 24699
    ScenePlayerSoundNotify = 20293
    TakeBattlePassMissionPointReq = 24391
    TakeInvestigationTargetRewardRsp = 25452
    PlayerPreEnterMpNotify = 22149
    SetBattlePassViewedRsp = 25281
    AvatarChangeCostumeReq = 28185
    HomeBasicInfoNotify = 20840
    AvatarExpeditionAllDataRsp = 3990
    SetUpAvatarTeamReq = 22244
    LevelupCityRsp = 4665
    HomeAllUnlockedBgmIdListNotify = 22324
    ActivityScheduleInfoNotify = 28401
    DungeonChallengeFinishNotify = 753
    AvatarFetterLevelRewardReq = 1484
    DelMailReq = 8496
    GetActivityInfoReq = 9710
    HomeAvatarSummonAllEventNotify = 22990
    TakeCompoundOutputReq = 5837
    GetAllUnlockNameCardRsp = 2632
    AvatarSkillDepotChangeNotify = 568
    AvatarPromoteRsp = 26699
    AvatarGainFlycloakNotify = 6824
    TakeAchievementRewardRsp = 8024
    DungeonCandidateTeamChangeAvatarReq = 1619
    PlayerChatNotify = 25824
    SkipPlayerGameTimeRsp = 29633
    WorldOwnerBlossomBriefInfoNotify = 24777
    GetDungeonEntryExploreConditionReq = 2592
    ActivityInfoNotify = 29575
    WorldOwnerDailyTaskNotify = 9896
    SceneInitFinishRsp = 24671
    DailyTaskFilterCityReq = 21803
    DoGachaReq = 22082
    GachaWishReq = 5636
    SetPlayerPropReq = 23363
    MonsterSummonTagNotify = 7831
    ChallengeDataNotify = 25295
    TakeBattlePassMissionPointRsp = 23201
    ChangeTeamNameRsp = 27356
    PlayerLoginRsp = 27771
    AddNoGachaAvatarCardNotify = 7037
    SetCoopChapterViewedRsp = 23389
    EntityFightPropUpdateNotify = 6590
    GetFriendShowAvatarInfoRsp = 27251
    AvatarSkillMaxChargeCountNotify = 9198
    GetProfilePictureDataRsp = 1846
    AvatarExpeditionCallBackRsp = 22955
    PlayerEnterDungeonReq = 7557
    ChooseCurAvatarTeamRsp = 6895
    GetBargainDataRsp = 8330
    EndCameraSceneLookNotify = 4771
    HomeSceneJumpReq = 5317
    FurnitureMakeStartReq = 27509
    BargainOfferPriceReq = 23582
    MusicGameStartRsp = 6458
    UnionCmdNotify = 9762
    EnterSceneDoneReq = 4561
    CodexDataFullNotify = 2558
    HomeGetOnlineStatusRsp = 23465
    SetPlayerNameReq = 9269
    GetScenePointReq = 23449
    UseItemRsp = 7672
    HomeEnterEditModeFinishReq = 9796
    GetPlayerBlacklistRsp = 23797
    HostPlayerNotify = 2109
    PingReq = 5983
    PersonalSceneJumpReq = 25750
    AvatarSkillInfoNotify = 28706
    AbilityInvocationsNotify = 3901
    DungeonCandidateTeamChangeAvatarRsp = 451
    TakeAchievementRewardReq = 29798
    AvatarPromoteReq = 20441
    GetAllUnlockNameCardReq = 5009
    TakeCompoundOutputRsp = 28960
    GetActivityInfoRsp = 7719
    GetDungeonEntryExploreConditionRsp = 26570
    SkipPlayerGameTimeReq = 8747
    AvatarGainCostumeNotify = 25978
    UnlockTransPointReq = 24297
    ProudSkillExtraLevelNotify = 5863
    LevelupCityReq = 25231
    SetUpAvatarTeamRsp = 306
    PlayerInvestigationAllInfoNotify = 1519
    ClientAbilitiesInitFinishCombineNotify = 4338
    AvatarExpeditionAllDataReq = 24160
    AvatarFetterDataNotify = 4274
    AvatarChangeCostumeRsp = 3408
    ObstacleModifyNotify = 2384
    SetBattlePassViewedReq = 4006
    QuestUpdateQuestVarNotify = 29565
    TakeInvestigationTargetRewardReq = 20048
    DelMailRsp = 26121
    AvatarFetterLevelRewardRsp = 9717
    HomeAvatarAllFinishRewardNotify = 9322
    ServerTimeNotify = 28606
    WorldPlayerInfoNotify = 27949
    GivingRecordNotify = 5883
    HomeChooseModuleReq = 8855
    AvatarDieAnimationEndReq = 943
    TryEnterHomeReq = 29384
    H5ActivityIdsNotify = 28482
    HomeChangeEditModeReq = 22458
    ServerAnnounceNotify = 25165
    HomeChangeBgmReq = 4543
    SetUpLunchBoxWidgetRsp = 24393
    BlossomBriefInfoNotify = 24748
    NpcTalkRsp = 23865
    HomeUpdateArrangementInfoReq = 344
    PullRecentChatRsp = 26725
    PlayerPropNotify = 25998
    GetUgcReq = 3704
    ReliquaryDecomposeReq = 25206
    AvatarUpgradeReq = 24626
    DungeonWayPointActivateReq = 7942
    TakeInvestigationRewardRsp = 4841
    ReliquaryUpgradeReq = 9142
    PlayerDataNotify = 7961
    VehicleInteractReq = 25867
    SetPlayerBirthdayReq = 26726
    CheckUgcStateReq = 3955
    HomeKickPlayerRsp = 1719
    CoopDataNotify = 21157
    ToTheMoonQueryPathReq = 6117
    FleurFairMusicGameSettleRsp = 23871
    HomeAvatarSummonFinishReq = 24791
    TowerLevelEndNotify = 22669
    DoSetPlayerBornDataNotify = 5351
    SetFriendEnterHomeOptionRsp = 21101
    ClientLockGameTimeNotify = 7730
    HomeResourceTakeHomeCoinRsp = 21855
    UpdatePlayerShowNameCardListRsp = 8022
    PlayerChatReq = 21209
    ForgeGetQueueDataRsp = 7571
    FurnitureCurModuleArrangeCountNotify = 21517
    LaunchFireworksReq = 6285
    WeaponAwakenReq = 25056
    SceneAvatarStaminaStepReq = 27101
    BatchBuyGoodsRsp = 8097
    PlayerSetPauseRsp = 25030
    BuyGoodsRsp = 22736
    HomeGetArrangementInfoReq = 24996
    ServerAnnounceRevokeNotify = 23231
    CutSceneBeginNotify = 455
    GetPlayerSocialDetailRsp = 1771
    ExecuteGadgetLuaReq = 29143
    DeleteFriendReq = 26120
    AvatarTeamUpdateNotify = 28759
    DealAddFriendRsp = 29289
    GetInvestigationMonsterRsp = 21253
    AllWidgetDataNotify = 9546
    EvtBulletDeactiveNotify = 28844
    GetAllH5ActivityInfoReq = 4793
    StartCoopPointReq = 22463
    HomeSaveArrangementNoChangeReq = 23493
    ReformFireworksReq = 3254
    PlayerPropChangeReasonNotify = 25374
    FurnitureMakeReq = 25118
    TakeBattlePassRewardRsp = 3069
    ForgeQueueManipulateRsp = 24425
    ChangeMpTeamAvatarRsp = 23226
    WidgetDoBagReq = 1993
    PlayerApplyEnterHomeResultReq = 20101
    EvtDoSkillSuccNotify = 1941
    DungeonWayPointNotify = 27604
    HomeAvatarSummonEventReq = 27629
    AskAddFriendRsp = 3297
    QuestListNotify = 23350
    AvatarEquipChangeNotify = 6767
    WearEquipRsp = 3218
    GetMailItemReq = 8354
    AvatarChangeElementTypeRsp = 26227
    TowerTeamSelectReq = 28157
    SceneTeamUpdateNotify = 29107
    OtherPlayerEnterHomeNotify = 22683
    AvatarExpeditionGetRewardReq = 4847
    GetWorldMpInfoRsp = 1461
    EvtCreateGadgetNotify = 21187
    TowerFloorRecordChangeNotify = 1981
    SyncScenePlayTeamEntityNotify = 26946
    EnterTransPointRegionNotify = 20259
    WidgetGadgetAllDataNotify = 26345
    PersonalLineAllDataRsp = 20607
    PlayerCookRsp = 1250
    PlayerWorldSceneInfoListNotify = 8028
    SetPlayerHeadImageRsp = 21563
    PlayerInvestigationNotify = 6848
    PlayerCookArgsReq = 7878
    AddQuestContentProgressReq = 20088
    PlayerGetForceQuitBanInfoRsp = 8368
    WeaponUpgradeRsp = 3294
    SceneEntityDrownReq = 23233
    PlayerQuitFromHomeNotify = 3135
    UnlockedFurnitureFormulaDataNotify = 28859
    GetPlayerFriendListReq = 21607
    RobotPushPlayerDataNotify = 23031
    CalcWeaponUpgradeReturnItemsRsp = 20136
    DungeonSlipRevivePointActivateReq = 28862
    CreateVehicleReq = 9915
    GetDailyDungeonEntryInfoRsp = 3265
    GetFriendShowNameCardInfoRsp = 1685
    EntityAiKillSelfNotify = 4703
    HomeChangeModuleRsp = 9924
    ForgeStartReq = 2720
    ForgeFormulaDataNotify = 8543
    PlayerCompoundMaterialRsp = 4656
    EnterSceneReadyRsp = 7914
    GetOnlinePlayerListRsp = 9049
    EvtDestroyGadgetNotify = 1452
    WorldPlayerRTTNotify = 2845
    AvatarSkillChangeNotify = 9268
    EvtAvatarSitDownNotify = 26530
    HomeResourceNotify = 28318
    HomeLimitedShopBuyGoodsReq = 838
    ActivityTakeWatcherRewardRsp = 2165
    SeeMonsterReq = 25646
    PlatformChangeRouteNotify = 28607
    PathfindingEnterSceneRsp = 2373
    EvtBulletHitNotify = 2465
    ClientLoadingCostumeVerificationNotify = 22940
    SceneAudioNotify = 7184
    SetWidgetSlotReq = 22701
    TowerMiddleLevelChangeTeamNotify = 20682
    GetShopRsp = 5665
    QuestDestroyNpcReq = 1472
    ReadPrivateChatReq = 24013
    CheckUgcUpdateReq = 8229
    GetAuthkeyReq = 20204
    SetEntityClientDataNotify = 5306
    DailyTaskDataNotify = 9714
    BuyBattlePassLevelReq = 20941
    CancelCoopTaskReq = 27925
    UnlockPersonalLineRsp = 5048
    GroupSuiteNotify = 4742
    SetPlayerSignatureReq = 1006
    TowerAllDataRsp = 2253
    StoreItemDelNotify = 27723
    DungeonRestartRsp = 26758
    DungeonEntryInfoRsp = 27112
    QuestProgressUpdateNotify = 28348
    HomeTransferReq = 2203
    GadgetInteractReq = 26009
    UnlockedFurnitureSuiteDataNotify = 21457
    ClientAIStateNotify = 22734
    AvatarUnlockTalentNotify = 1893
    DungeonPlayerDieReq = 7032
    TrialAvatarFirstPassDungeonNotify = 8103
    EntityFightPropChangeReasonNotify = 7107
    SetPlayerBornDataRsp = 26454
    WorldDataNotify = 23950
    GetActivityShopSheetInfoRsp = 4109
    SceneTransToPointRsp = 24104
    WorldPlayerLocationNotify = 7420
    TowerCurLevelRecordChangeNotify = 8595
    PlayerHomeCompInfoNotify = 20264
    ChangeAvatarRsp = 2046
    MailChangeNotify = 27744
    ResinChangeNotify = 4336
    BargainStartNotify = 9154
    GetUgcBriefInfoRsp = 25183
    SelectWorktopOptionRsp = 1697
    ItemAddHintNotify = 26599
    UpdatePlayerShowAvatarListReq = 3998
    PrivateChatReq = 24426
    EntityAiSyncNotify = 24710
    EnterTrialAvatarActivityDungeonRsp = 8751
    SetChatEmojiCollectionReq = 1123
    AvatarExpeditionStartReq = 751
    MusicGameSettleReq = 24309
    GetFurnitureCurModuleArrangeCountReq = 22795
    QueryCodexMonsterBeKilledNumReq = 21437
    TowerEnterLevelRsp = 5746
    FleurFairMusicGameStartReq = 5303
    AddBackupAvatarTeamRsp = 7930
    ServerBuffChangeNotify = 21009
    BuyResinRsp = 3650
    GadgetStateNotify = 21201
    CombineRsp = 492
    GetSceneAreaReq = 8189
    ScenePlayerLocationNotify = 29696
    PullPrivateChatReq = 8925
    HomeAvatarRewardEventGetReq = 7571
    QuestCreateEntityReq = 28703
    GetMapAreaRsp = 22235
    PSPlayerApplyEnterMpRsp = 21696
    SetNameCardRsp = 27175
    EvtAvatarLockChairReq = 8990
    RogueDiaryDungeonSettleNotify = 27081
    ReceivedTrialAvatarActivityRewardRsp = 9311
    HomeAvatarRewardEventNotify = 1329
    PlatformStopRouteNotify = 25803
    HomeModuleSeenRsp = 5790
    HomePreChangeEditModeNotify = 3607
    MarkMapReq = 9550
    PostEnterSceneRsp = 22743
    DelBackupAvatarTeamRsp = 5780
    GetGachaInfoReq = 7728
    UnlockAvatarTalentRsp = 22369
    EnterWorldAreaReq = 479
    SetOpenStateReq = 24291
    EvtAvatarStandUpNotify = 28594
    HomeMarkPointNotify = 22396
    AvatarSkillUpgradeReq = 22618
    GetChatEmojiCollectionReq = 25164
    PrivateChatNotify = 6396
    GetPlayerTokenRsp = 24174
    WorldPlayerReviveRsp = 22159
    HomeResourceTakeFetterExpRsp = 22038
    TakeFurnitureMakeReq = 7585
    GetRegionSearchReq = 27191
    GetPlayerAskFriendListReq = 1813
    AvatarWearFlycloakReq = 243
    TowerLevelStarCondNotify = 29627
    WorldPlayerDieNotify = 2689
    WeaponPromoteRsp = 23521
    WindSeedType1Notify = 7486
    GetWidgetSlotReq = 9388
    QuickUseWidgetReq = 1372
    GetHomeLevelUpRewardReq = 2113
    TowerEnterLevelReq = 20408
    QueryCodexMonsterBeKilledNumRsp = 28880
    MusicGameSettleRsp = 7327
    AvatarExpeditionStartRsp = 28415
    SetChatEmojiCollectionRsp = 2098
    CombineFormulaDataNotify = 22050
    CookRecipeDataNotify = 21778
    HomeGetBasicInfoReq = 9267
    DailyTaskUnlockedCitiesNotify = 6722
    EnterTrialAvatarActivityDungeonReq = 7738
    QuestCreateEntityRsp = 9887
    ProudSkillChangeNotify = 26650
    HomeAvatarRewardEventGetRsp = 5969
    PullPrivateChatRsp = 29160
    AchievementUpdateNotify = 27625
    GetSceneAreaRsp = 27301
    CombineReq = 3349
    PlayerApplyEnterHomeResultNotify = 26518
    AddBackupAvatarTeamReq = 22689
    FleurFairMusicGameStartRsp = 21453
    ChangeAvatarReq = 3470
    HomeModuleUnlockNotify = 27507
    ServerCondMeetQuestListUpdateNotify = 9044
    UpdatePlayerShowAvatarListRsp = 20659
    ShowCommonTipsNotify = 28414
    BattlePassMissionUpdateNotify = 3190
    DungeonSettleNotify = 8007
    SelectWorktopOptionReq = 23125
    TakeAchievementGoalRewardRsp = 8945
    FinishedParentQuestUpdateNotify = 28362
    ToTheMoonEnterSceneReq = 6116
    GetUgcBriefInfoReq = 4301
    AchievementAllDataNotify = 259
    AvatarLifeStateChangeNotify = 4653
    HomeResourceTakeFetterExpReq = 4383
    WorldPlayerReviveReq = 2401
    GetPlayerTokenReq = 6013
    PlayerTimeNotify = 2272
    GetChatEmojiCollectionRsp = 26849
    EvtAvatarUpdateFocusNotify = 3013
    UnfreezeGroupLimitNotify = 2540
    AvatarTeamAllDataNotify = 22603
    AvatarSkillUpgradeRsp = 26538
    ChapterStateNotify = 25075
    GetHomeLevelUpRewardRsp = 21591
    SceneEntityDisappearNotify = 29127
    QuickUseWidgetRsp = 22155
    GetWidgetSlotRsp = 5441
    EnterScenePeerNotify = 9626
    WeaponPromoteReq = 9611
    AvatarWearFlycloakRsp = 27660
    GetPlayerAskFriendListRsp = 3915
    TakeFurnitureMakeRsp = 28114
    VehicleStaminaNotify = 1047
    WorktopOptionNotify = 28583
    DelBackupAvatarTeamReq = 20273
    PostEnterSceneReq = 3633
    MarkMapRsp = 21436
    EvtAiSyncCombatThreatInfoNotify = 2682
    HomeModuleSeenReq = 24019
    ReadMailNotify = 23556
    ReceivedTrialAvatarActivityRewardReq = 8615
    EvtAvatarLockChairRsp = 5831
    SetNameCardReq = 20106
    QuestTransmitRsp = 2300
    PSPlayerApplyEnterMpReq = 3109
    ShowClientGuideNotify = 8965
    SetOpenStateRsp = 7944
    EnterWorldAreaRsp = 7481
    UnlockAvatarTalentReq = 21301
    GetGachaInfoRsp = 9090
    HomeAvatarTalkFinishInfoNotify = 20880
    BattlePassCurScheduleUpdateNotify = 1819
    PlayerCompoundMaterialReq = 26870
    GCGTCTavernChallengeDataNotify = 7499
    ForgeStartRsp = 24460
    SceneTimeNotify = 29187
    SceneAreaUnlockNotify = 25419
    ForgeDataNotify = 6985
    HomeChangeModuleReq = 26930
    QuestListUpdateNotify = 3344
    GetFriendShowNameCardInfoReq = 29743
    AvatarFlycloakChangeNotify = 28644
    CreateVehicleRsp = 22592
    DungeonSlipRevivePointActivateRsp = 24625
    CalcWeaponUpgradeReturnItemsReq = 20664
    ActivityTakeWatcherRewardReq = 23105
    HomeLimitedShopBuyGoodsRsp = 6986
    DungeonPlayerDieNotify = 28876
    BargainTerminateNotify = 28886
    SyncTeamEntityNotify = 29231
    HomeAvatarTalkRsp = 213
    GetOnlinePlayerListReq = 27044
    EnterSceneReadyReq = 20524
    SetPlayerHeadImageReq = 21526
    UpdateAbilityCreatedMovingPlatformNotify = 6778
    PlayerCookReq = 27404
    PersonalLineAllDataReq = 28403
    ScenePlayerInfoNotify = 7477
    GetWorldMpInfoReq = 6964
    AvatarExpeditionGetRewardRsp = 25237
    PlayerEnterSceneInfoNotify = 26700
    GetPlayerFriendListRsp = 893
    AskAddFriendNotify = 5432
    PlayerApplyEnterMpNotify = 5245
    ForgeQueueDataNotify = 5698
    SceneEntityDrownRsp = 1742
    ClientAbilityChangeNotify = 27339
    WeaponUpgradeReq = 24162
    PlayerGetForceQuitBanInfoReq = 24478
    AddQuestContentProgressRsp = 22640
    PlayerCookArgsRsp = 9840
    AbilityChangeNotify = 22133
    PlayerQuitDungeonReq = 25440
    StoreWeightLimitNotify = 3034
    OpenStateChangeNotify = 26658
    PlayerEnterSceneNotify = 3595
    SceneAreaWeatherNotify = 21395
    DailyTaskProgressNotify = 27206
    GadgetInteractRsp = 28160
    EvtAiSyncSkillCdNotify = 28128
    SumoDungeonSettleNotify = 23188
    AvatarPropNotify = 21114
    AntiAddictNotify = 243
    SceneTransToPointReq = 4027
    GetActivityShopSheetInfoReq = 24121
    FinishedParentQuestNotify = 25902
    SetPlayerBornDataReq = 25726
    HitTreeNotify = 20542
    CheckUgcUpdateRsp = 28411
    QuestDestroyNpcRsp = 23800
    GetShopReq = 4619
    UnlockNameCardNotify = 3896
    PlayerPropChangeNotify = 27937
    PlayerInvestigationTargetNotify = 5321
    GadgetAutoPickDropInfoNotify = 28191
    AvatarDataNotify = 23378
    SetWidgetSlotRsp = 7049
    ClientScriptEventNotify = 1503
    PathfindingEnterSceneReq = 2374
    SceneKickPlayerRsp = 27200
    ChangeMailStarNotify = 29855
    DungeonEntryInfoReq = 6446
    DungeonRestartReq = 29252
    TowerAllDataReq = 2265
    SetPlayerSignatureRsp = 24101
    CancelCoopTaskRsp = 26816
    UnlockPersonalLineReq = 1085
    BuyBattlePassLevelRsp = 23240
    GetAuthkeyRsp = 383
